# 🍱 Today-Meal (오늘의 급식 자동 카드뉴스 생성기)

> **나이스(NEIS) 오픈API**로부터 당일 급식 메뉴를 실시간으로 조회하고, 인스타그램 스토리 및 피드 규격(**1080×1080**)의 이미지로 자동 제작해 주는 파이썬 유틸리티입니다.

---

## 📌 주요 기능

- ⚡ **실시간 NEIS 급식 조회**: 교육부 나이스 교육정보 개방포털의 `mealServiceDietInfo` OpenAPI를 통해 당일 급식 데이터를 실시간 파싱
- 🧹 **스마트 텍스트 정제**:
  - 알레르기 유발 정보(괄호 숫자 번호) 자동 제거
  - 불필요한 특수문자 및 태그 정제 후 순수 메뉴명 추출
- 🎨 **1080×1080 인스타그램 규격 렌더링**:
  - 원하는 배경색(Hex) 및 폰트 컬러 자유 지정
  - 트루타입 폰트(TTF) 기반의 고화질 이미지 생성
- 📝 **텍스트/이미지 동시 출력**:
  - 정제된 메뉴 텍스트를 파일로 기록(`txt`)함과 동시에 최종 카드뉴스 이미지(`png`) 생성

---

## 🛠️ 기술 스택 및 요구 사양

- **언어**: Python 3.8 이상
- **의존 라이브러리**:
  - `requests`: NEIS OpenAPI 통신
  - `beautifulsoup4`: XML 데이터 파싱
  - `Pillow` (PIL): 카드뉴스 이미지 합성 및 텍스트 렌더링

---

## 🚀 빠른 시작 (Quick Start)

### 1. 필수 라이브러리 설치

```bash
pip install requests beautifulsoup4 pillow
```

### 2. 설정값 입력 (`main(github).py`)

스크립트 상단의 설정 변수에 본인의 환경에 맞는 값을 입력합니다.

```python
# =========================================== 학교코드 ===========================================
# 시도교육청코드 (예: 서울특별시교육청 'B10')
SC_CODE = "B10"

# 행정표준코드 (예: 7자리 학교 고유 코드)
SD_CODE = "7010536"

# ================================ 파일위치 (역슬래시 2번씩) =================================
# 메뉴 텍스트 임시 저장 경로
txtfile = "C:\\path\\to\\meal.txt"

# 최종 생성될 PNG 이미지 경로
pngfile = "C:\\path\\to\\today_meal.png"

# 사용할 트루타입 폰트(.ttf) 파일 경로
fontfile = "C:\\Windows\\Fonts\\malgun.ttf"

# ===================================== 색상 (HEXCODE) ========================================
# 배경 색상
backclr = "#FFFFFF"

# 글자 색상
txtclr = "#1F2937"
```

> [!TIP]
> **학교 코드 확인 방법**:
> [나이스 교육정보 개방포털](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17020190531110010104913&infSeq=1#none)에서 본인의 학교를 검색하여 **시도교육청코드(`ATPT_OFCDC_SC_CODE`)**와 **표준학교코드(`SD_SCHUL_CODE`)**를 확인할 수 있습니다.

### 3. 실행

```bash
python "main(github).py"
```

실행이 완료되면 지정한 경로에 `today_meal.png` 이미지가 생성됩니다.

---

## 📁 프로젝트 구조

```
today-meal/
├── README.md           # 프로젝트 문서
├── requirements.txt    # 의존성 패키지 목록
└── main(github).py     # 급식 조회 및 이미지 생성 메인 스크립트
```

---

## 🧭 로드맵 (향후 개선 계획)

- [ ] `instagrapi` 등을 활용한 인스타그램 스토리 자동 업로드 파이프라인 구축
- [ ] 디스코드(Discord) / 카카오톡 알림 봇 연동
- [ ] 메뉴 수에 따른 자동 폰트 크기/행간 조절 (텍스트 오버플로우 방지)
- [ ] 하드코딩된 설정값을 `.env` 또는 `config.json`으로 분리

---

## 👤 연락처

- **Discord**: `dotori_007`
- **GitHub**: [@dotori-007](https://github.com/dotori-007)
