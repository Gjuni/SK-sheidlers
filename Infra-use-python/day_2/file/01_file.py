import os as os

current_directory = os.getcwd()
print(f"current work directory : {current_directory}")

file_path = 'C:\\Users\\ez\\Desktop\\Code\\Sk Sheiders\\SK-sheidlers\\Infra-use-python\\file.txt'

## 파일을 다룰 때 os.path를 많이 사용함.
## 파일에 대해서 사이즈, 변경 사항, 접근 하였는지 확인할 수 있는 method가 있음 (getatime, getctime, getsize)
if os.path.isfile(file_path): # 파일이냐? 디렉터리이냐?
    print(f"{file_path}는 파일이다!!")
elif os.path.isdir(file_path): # 함수 호출로 변경
    print(f"{file_path}는 디렉토리이다!") ## 왜 디렉토리라고 나옴??