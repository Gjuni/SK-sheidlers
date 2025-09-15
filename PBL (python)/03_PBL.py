## 서버에 업로드 되는 파일에 개인정보 포함 유무를 모니터링 하고 싶다.

# 조건
## 1. 디렉토리에 새로운 파일의 추가를 반지
## 2. 추가될 경우 즉시 이를 감지하고 결과를 출력
## 3. 추가된 파일 내에 중요 정보 (주석 처리된 텍스트, 이베일 주소)가 포함되어 있다면 이를 확인하고 처리

# 처리해야할 부분
## 주석 처리된 텍스트 startwith("#, //")
## 이메일 주소 포함

# 출력 결과
## 탐지된 파일명
## 처리해야할 부분에서의 값이 존재하다면 줄 번호와 해당 내용을 출력

import os
import time
import re

## 전역 변수 선언
cur_path = os.getcwd()
pre_file_list = []


## 현 디렉토리 체크
def check_directory() :
    global pre_file_list
    pre_file_list = os.listdir(cur_path)

## 모니터링 함수
def mornitoring():
    global pre_file_list

    while(True):
        changed_file_list = os.listdir(cur_path)
        
        results  = set(changed_file_list) - set(pre_file_list)
        print(f"탐지 중입니다. {results}")
        
        if results :
            for result in results :
                print(f"file changed detected : {result}")
                check_file(result)

        pre_file_list = changed_file_list

        time.sleep(1)

## 파일 체크
def check_file(file) :
    with open (file, 'r', encoding='utf-8') as body:
        for index, line in enumerate(body.readlines()):
            general_expression(index+1, line)
    print("검사를 종료합니다.")

## 각 라인 검사.
def general_expression(index, line) :
    ## example123@gmail.com
    email_pattern = r'[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'
 
    ## 주석 검사   
    if(line.startswith('#') or line.startswith('//')) : 
        print(f"{index}번째 라인 주석 탐지 : {line}")
    ## 이메일 검사
    elif (re.findall(email_pattern, line)):
        print(f"{index}번째 라인 이메일 탐지 : {line}")


## 메인 함수
def main():
    global cur_path
    check_directory()
    mornitoring()

if __name__ == "__main__" :
    main()