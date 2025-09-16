# faker 
from faker import Faker
## 가짜 데이터 만들기
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['mydatabase_faker']
collection = db['people']

fake = Faker("ko_KR") ## 다국어 지원 데이터 생성

for _ in range(20): # 20개를 생성
    person = {
        "name" : fake.name(), ## 이름 생성
        "address" : fake.address(), ## 주소 생성
        "email" : fake.email(), ## 이메일 생성
        "phone" : fake.phone_number() ## 폰 번호 생성
    }
    collection.insert_one(person)

print("데이터 삽입 완료")