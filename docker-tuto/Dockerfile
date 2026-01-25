# 👉🏻 파이썬 3.10이 이미 깔려있는 기본 도커라는 가짜컴을 하나 만듬
FROM python:3.10-slim

# 👉🏻 도커라는 가짜컴 안에 앞으로 작업할 기본 폴더를 /app으로 설정.
# app이란 폴더 만들고 그 폴더 vscode로 연느낌
WORKDIR /app

# 의존성 설치
# 👉🏻왼쪽: 호스트(내 컴퓨터) / 오른쪽: 가짜컴(도커 컴퓨터)이라 보면됨
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 소스 복사
# 왼쪽: 호스트(내 컴퓨터) / 오른쪽: 가짜컴(도커 컴퓨터)
# 👉🏻현재 모든 코드를 다 복사해서, 도커컴에 app/ 폴더내에 그대로 복붙한다 보면됨
COPY . .

# 컨테이너 실행 시
# 1) pytest 실행
# 2) 성공하면 flask api 실행
# 👉🏻가짜컴(도커컴)에서 깃배쉬 열어서 아래 명령어 치고 수행한다 보면됨
CMD pytest && python app.py

# 🤔 RUN vs CMD 뭔 차이임?
# RUN은 이미지 만들 때 실행 (도커파일로 이미지 만들 때)
# CMD는 컨테이너 실행할 때 실행. (이미지 맨든거 실행할 때 실행)