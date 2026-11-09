# 🍱 Today-Meal (오늘의 급식 자동 카드뉴스 생성기)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)

> **나이스(NEIS) 오픈API**로부터 당일 급식 메뉴를 실시간으로 조회하고, 인스타그램 스토리 및 피드 규격(**1080×1080**)의 이미지로 자동 제작해 주는 파이썬 유틸리티입니다.

---

## 📌 주요 특징

- ⚡ **실시간 NEIS 급식 조회**: 교육부 나이스 교육정보 개방포털의 `mealServiceDietInfo` OpenAPI를 통해 당일 급식 데이터를 실시간 파싱
- 🧹 **스마트 텍스트 정제**:
  - 알레르기 유발 정보(괄호 숫자 번호) 자동 제거
  - 불필요한 특수문자 및 태그 정제 후 순수 메뉴명 추출
- 🎨 **1080×1080 인스타그램 규격 렌더링**:
  - 원하는 배경색(Hex) 및 폰트 컬러 자유 지정
  - 트루타입 폰트(TTF) 기반의 고화질 이미지 생성
- 🔒 **환경 변수(.env) 보안 격리**:
  - 학교 코드 및 출력 경로를 환경 변수 또는 `.env`로 안전하게 분리
- 📝 **텍스트/이미지 동시 출력**:
  - 정제된 메뉴 텍스트를 파일로 기록(`txt`)함과 동시에 최종 카드뉴스 이미지(`png`) 생성

---

## 🛠️ 기술 스택 및 요구 사양

- **언어**: Python 3.8 이상
- **의존 라이브러리**:
  - `requests`: NEIS OpenAPI 통신
  - `beautifulsoup4`: XML 데이터 파싱
  - `Pillow` (PIL): 카드뉴스 이미지 합성 및 텍스트 렌더링
  - `python-dotenv`: `.env` 환경 변수 관리

---

## 🚀 빠른 시작 (Quick Start)

### 1. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 2. 환경변수 설정 (`.env`)

`.env.example` 파일을 복사하여 `.env` 파일을 생성하고 본인의 학교 코드를 입력합니다:

```env
# 시도교육청코드 (예: 서울특별시교육청 'B10')
NEIS_SC_CODE=B10

# 행정표준코드 (예: 7자리 학교 고유 코드)
NEIS_SD_CODE=7010536

# 출력 파일 경로 (선택)
OUTPUT_TXT_PATH=meal.txt
OUTPUT_IMG_PATH=today_meal.png
FONT_PATH=C:\Windows\Fonts\malgun.ttf
BG_COLOR=#FFFFFF
TXT_COLOR=#1F2937
```

> [!TIP]
> **학교 코드 확인 방법**:
> [나이스 교육정보 개방포털](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17020190531110010104913&infSeq=1#none)에서 본인의 학교를 검색하여 **시도교육청코드(`ATPT_OFCDC_SC_CODE`)**와 **표준학교코드(`SD_SCHUL_CODE`)**를 확인할 수 있습니다.

### 3. 실행

```bash
# 기본 실행 (.env 설정값 적용)
python main.py

# 또는 커맨드라인 인자로 학교 코드 직접 전달
python main.py B10 7010536
```

실행이 완료되면 지정한 경로에 `today_meal.png` 이미지가 생성됩니다.

---

## 📁 프로젝트 구조

```
today-meal/
├── README.md           # 프로젝트 가이드 문서
├── LICENSE             # MIT 오픈소스 라이선스
├── .gitignore          # Git 제외 파일 목록
├── .env.example        # 환경변수 템플릿
├── requirements.txt    # 의존성 패키지 목록
├── main.py             # 환경변수/CLI 인자 지원 개선 메인 스크립트
└── main(github).py     # 기존 레거시 단독 스크립트
```

---

## 📄 저작권 및 공공데이터 라이선스 (License & Attribution)

- **코드 라이선스**: [MIT License](LICENSE) (Copyright (c) 2026 dotori-007)
- **공공데이터 출처**:
  - 본 프로그램에서 활용하는 급식 데이터는 **교육부 및 한국교육학술정보원(KERIS)**의 [나이스 교육정보 개방포털(NEIS OpenAPI)](https://open.neis.go.kr/) 공공데이터를 기반으로 합니다.
  - 공공데이터 제공 지침 및 이용조건을 준수합니다.
