import random
import string

def generate_random_name(length=5):
    """
    테스트용 랜덤 문자열을 생성합니다 (예: 'abcde')
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_test_email():
    """
    랜덤 이메일을 생성합니다 (예: 'abcde@test.com')
    """
    return f"{generate_random_name()}@test.com"

def generate_test_email2():
    """
    랜덤 이메일을 생성합니다 (예: 'abcde@test.com')
    """
    return f"{generate_random_name()}@test.com"

def generate_test_email3():
    """
    랜덤 이메일을 생성합니다 (예: 'abcde@test.com')
    """
    return f"{generate_random_name()}@test.com"