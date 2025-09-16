from pymongo import MongoClient

# MongoClient는 애플리케이션 전체에서 한 번만 생성하고 재사용하는 것이 좋습니다.
# 모듈이 로드될 때 클라이언트 인스턴스를 생성합니다.
client = MongoClient('mongodb://localhost:27017')

def get_db(database_name='userMongo'):
    return client[database_name]
