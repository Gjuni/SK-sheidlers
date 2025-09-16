from pymongo import MongoClient # mongo 접속 정보 들어감

client = MongoClient('mongodb://localhost:27017')

# mysql, mssql, oracle - 데이터베이스 > 테이블 > 컬럼 > 데이터
# mongodb - 데이터베이스 > 콜랙션(Collections) > 데이터
# Elastic Search - 인덱스 > 문서(Document) > 데이터...

db = client['school_db'] # 데이터베이스
collection = db['student'] # 콜랙션을 student로 쓰겠다.


## MongoDb는 Key : value 형식으로 삽입
student = {
    "name" : "홍길동",
    "age" : 20,
    "grade" : "A",
    "subject" : ["수학", "영어"]
}

students = [
    {"name": "이영희", "age": 19, "grade": "B", "subjects": ["과학", "국어"]},
    {"name": "박민수", "age": 21, "grade": "A", "subjects": ["수학", "과학"]}
]

## collection에 data 삽입
# result = collection.insert_one(student)
result = collection.insert_many(students)
# print(f"추가된 문서 : {result.inserted_id}") ## 현재 추가된 id 값을 가져와라
print(f"추가된 문서 : {result.inserted_ids}")