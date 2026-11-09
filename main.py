import os
import sys
import datetime
import requests
import re
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Configuration from Environment Variables or defaults
SC_CODE = os.environ.get("NEIS_SC_CODE", "B10")            # 시도교육청코드 (예: 서울 B10)
SD_CODE = os.environ.get("NEIS_SD_CODE", "")               # 행정표준코드 (7자리)
TXT_FILE = os.environ.get("OUTPUT_TXT_PATH", "meal.txt")
PNG_FILE = os.environ.get("OUTPUT_IMG_PATH", "today_meal.png")
FONT_FILE = os.environ.get("FONT_PATH", "C:\\Windows\\Fonts\\malgun.ttf")
BG_COLOR = os.environ.get("BG_COLOR", "#FFFFFF")
TXT_COLOR = os.environ.get("TXT_COLOR", "#1F2937")

def fetch_and_generate_meal_card(sc_code=SC_CODE, sd_code=SD_CODE):
    if not sd_code or sd_code == "ur code":
        print("[Notice] NEIS_SD_CODE is not specified in .env or arguments.")
        print("Usage: python main.py [SC_CODE] [SD_SCHUL_CODE]")
        sys.exit(1)

    today = datetime.date.today().strftime('%Y%m%d')
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?ATPT_OFCDC_SC_CODE={sc_code}&SD_SCHUL_CODE={sd_code}&MLSV_YMD={today}"

    print(f"[*] Querying NEIS Meal API for date: {today}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[Error] Failed to connect to NEIS API: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.content, "xml")
    data = soup.get_text().replace("<br/>", "")
    td_dataset = []
    for line_no, line in enumerate(data.splitlines()):
        if line_no == 17:
            td_dataset.append(line)

    if not td_dataset:
        print("[!] No meal information found for today (Holiday or Weekend).")
        return

    mfilter = td_dataset[0].split("1.") if "1." in td_dataset[0] else [td_dataset[0]]
    cleaned_menus = []
    for i in range(1, len(mfilter)):
        menu = mfilter[i].strip()
        menu = re.sub(r"\(.*?\)", "", menu).strip("()")
        menu = re.sub(r"[^가-힣]", "", menu)
        if menu:
            cleaned_menus.append(menu)

    # Save to text file
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        for menu in cleaned_menus:
            f.write(f"{menu}\n")
            print(f"  - {menu}")

    # Generate Image (1080x1080 Instagram format)
    img = Image.new("RGB", (1080, 1080), BG_COLOR)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_FILE, 70)
    except Exception:
        font = ImageFont.load_default()

    start_y = 150
    line_height = 100
    for idx, menu in enumerate(cleaned_menus):
        draw.text((100, start_y + (line_height * idx)), menu, font=font, fill=TXT_COLOR)

    img.save(PNG_FILE)
    print(f"[+] Successfully generated meal card: {PNG_FILE}")

if __name__ == "__main__":
    arg_sc = sys.argv[1] if len(sys.argv) > 1 else SC_CODE
    arg_sd = sys.argv[2] if len(sys.argv) > 2 else SD_CODE
    fetch_and_generate_meal_card(arg_sc, arg_sd)
