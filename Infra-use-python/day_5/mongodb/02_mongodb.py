from pymongo import MongoClient # mongo 접속 정보 들어감

client = MongoClient('mongodb://localhost:27017')

db = client['school_db'] # 데이터베이스
collection = db['student'] # 콜랙션을 student로 쓰겠다.

# for studnet in collection.find() : # find는 전체 데이터 가져옴.
    # print(studnet)


print(collection.find_one({"name" : "홍길동"}))

for student in collection.find({"age": {"$gte" : 20}}) :
    print(student)