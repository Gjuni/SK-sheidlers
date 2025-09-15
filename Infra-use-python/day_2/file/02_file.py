import os as os

files = os.listdir('.') # 현재 디렉터리의 파일과 디렉터리 목록을 리스트로 반환
print(files) # . 은 현재 디렉토리
## listdir은 파일인지 디렉토리인지 구분하지 않음

## 파일과 디렉터리 구분 예외처리 해줘야함. list로 반환한기 때문에 파일이지 디렉토리인지 구분 불가
for file in files:
    if os.path.isfile(file):
        print(f"{file}는 파일입니다.")
    elif os.path.isdir(file):
        print(f"{file}는 디렉토리입니다.")
        ## 디렉토리이면 또 그 안에 파일과 디렉토리가 있을 수 있음


files = os.walk('C:\\Users\\ez\\Desktop\\Code\\Sk Sheiders\\SK-sheidlers\\Infra-use-python') # 현재 디렉터리의 파일과 디렉터리 목록을 리스트로 반환

for dirpath, dirnames, filenames in files:
    print(f"디렉토리 경로: {dirpath}")
    print(f"디렉토리 이름들: {dirnames}")
    print(f"파일 이름들: {filenames}")
    print()