import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_check_first_post_title():
    """
    1번 포스트의 제목이 비어있지 않은지 확인하는 테스트
    """
    # 1. API 호출
    response = requests.get(f"{BASE_URL}/1")
    
    # 2. 결과(JSON) 변환
    data = response.json()
    
    # 3. 검증 (상태코드 200인지, 제목이 있는지)
    assert response.status_code == 200
    assert "title" in data
    assert len(data["title"]) > 0
    
    ## 확인중....