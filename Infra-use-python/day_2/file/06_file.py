#day2 폴더를 모니터링(감시)
#새로운 파일이 업로드가 되면 탐지!!
#(ToDo) 업로드된 새로운 파일에 개인정보가 포함되면 탐지!!

import os as os
import time as time
from datetime import datetime

dir_path = 'C:\\Users\\ez\\Desktop\\Code\\Sk Sheiders\\SK-sheidlers\\Infra-use-python\\day_2'

## 탐지하기 이전의 파일 목록 저장
pre_file = set(os.listdir(dir_path)) # 리스트 형태는 (cur_file - pre_file) 이 불가능함. 그래서 set을 사용

for index, filename in enumerate(pre_file):
    print(f"{index} : {filename}")
    

while(True) :
    cur_file = set(os.listdir(dir_path)) # set끼리 연산 가능하며 중복 제거를 위해서 TypeCasting을 함.

    result = cur_file - pre_file

    print(f"{result}")
    time.sleep(1)

    pre_file = cur_file

    ## 탐지된 파일 보고서에 추가
    for i in result :
        now_date = datetime.now()
        now_day = datetime.now().strftime("%Y-%m-%d")
        now_hour = datetime.now().strftime("%H:%M:%S")

        with open(f"{now_day}_보고서.txt", 'a', encoding='utf-8') as file:
            file.write(f"작성자 : Jun\n")
            file.write(f"주요 내용 : 파일 탐지\n")
            file.write(f"파일명 : {i}\n")
            file.write(f"추가 시간 : {now_hour}\n")
            file.write(f"========================\n\n")


    for i in result:
        full_path = os.path.join(dir_path, i)

        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

            for index, body in enumerate(content):
                print(f"{index} : {body}")