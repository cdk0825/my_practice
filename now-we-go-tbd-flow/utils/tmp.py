# utils 폴더 안의 generator.py 파일에서 함수들을 가져옵니다.
from utils.generator import generate_random_name, generate_test_email

def run_example():
    print("--- 랜덤 데이터 생성 예제 시작 ---")

    # 1. 랜덤 이름 생성 함수 사용
    random_name = generate_random_name(8)  # 8글자 랜덤 이름 요청
    print(f"생성된 랜덤 이름: {random_name}")

    # 2. 랜덤 이메일 생성 함수 사용
    random_email = generate_test_email()
    print(f"생성된 랜덤 이메일: {random_email}")

    print("--- 예제 종료 ---")

if __name__ == "__main__":
    run_example()