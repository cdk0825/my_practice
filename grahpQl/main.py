import strawberry
from typing import List

'''
로컬에서 그래프Ql 사용하기.
실행할 그래프ql 파일 위치로 이동
python -m strawberry dev main 서버 실행 명령어실행
http://0.0.0.0:8000/graphql 으로 실행하라고 설명하지만
실질적으로 http://loalhost:8000/graphql 으로 실행해야 접속가능함
또는 http://127.0.0.1:8000/graphql 으로 접속
'''

# 1. 데이터 구조 정의(Schema)
@strawberry.type
class User:
    name: str
    age: int
    
# 샘플 제이터
USER_DATA = [
    User(name="제미나이", age=2),
    User(name="홍길동", age=30),
]

# 2. 데이터를 가져오는 방식 정의 (Query)
@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> List[User]:
        return USER_DATA
    
    @strawberry.field
    def search_user(self, name: str) -> User:
        for user in USER_DATA:
            if user.name == name:
                return user
        return None
    
    # 🔴 여기 (age: int = None) 이 부분이 반드시 추가되어야 합니다!
    @strawberry.field
    def get_users(self, age: int = None) -> List[User]:
        if age is not None:
            return [user for user in USER_DATA if user.age == age]
        return USER_DATA
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, age: int) -> User:
        new_user = User(name=name, age=age)
        USER_DATA.append(new_user)
        return new_user

# 3. 스키마 및 서버 설정
schema = strawberry.Schema(query=Query, mutation=Mutation)
    
    
'''
브라우저 테스트 
- 쿼리 입력값

(나이)
query FilteredUsers($inputAge: Int) {
  getUsers(age: $inputAge) {
    name
    age
  }
}
(이름)
query FilteredUsers($inputName: String!) {
  searchUser(name: $inputName) {
    name
    age
  }
}

-Variable 입력값
(나이)
{
  "inputAge": 30
}
(이름)
{
  "inputName": "홍길동"
}


-데이터 추가
mutation CreateNewUser($newName: String!, $newAge: Int!) {
  addUser(name: $newName, age: $newAge) {
    name
    age
  }
}

{
  "newName": "김철수",
  "newAge": 25
}
'''