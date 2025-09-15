import os

file_path = 'C:\\Users\\ez\\Desktop\\Code\\Sk Sheiders\\SK-sheidlers\\Infra-use-python'

all_files = os.listdir(file_path)

# 임시 저장
txt_file = []

for file in all_files:
    if file.endswith('.txt'):
        ## 추가해라
        txt_file.append(file)

print(txt_file)

for i in txt_file : # 업로드된 txt 파일 이름을 가져오는 것 
    ## 이름만 읽게 되면 디렉토리에 존재하지 않기 때문에 전체 path를 합쳐서 전달해줘야한다.
    ## infra-use-python 이라는 디렉토리 .txt 파일을 가져오는데 이름만 존재하면 어디 디렉토리의 파일을 가져오는지 모르기 때문에 합쳐서 전달해야함.

    full_path = os.path.join(file_path, i)
    with open(full_path, 'r', encoding='utf-8') as cur_file:
        content = cur_file.read()
        print(f"파일 내용 : {content}")
        print("**********************\n")


print("라인 별 검사 로직 추가")
### 파일 앞쪽에 #나 // 주석처리 된 것을 찾아내시오. startwith('')
### 출력 예제는 "파일이름 : 1번째 라인 탐지 : 내용"

for i in txt_file:
    full_path = os.path.join(file_path, i)
    with open(full_path, 'r', encoding='utf-8') as cur_file:
        content = cur_file.readlines()
        
        ### enumerate 사용해서 index 지우고 refactoring해야함.
        index = 1
    
        for t in content :
            if(index is 1) :
                print(f"파일이름 : {i}")
            if(t.startswith('#') or t.startswith('//')) :
                print(f"{index}번째 라인 탐지 : {t.strip()}")
            index += 1
