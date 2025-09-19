## FTP 자동화 
## IT부터의 개발자로서 회사 내부에서 사용하는 중요한 파일들을 정기적으로 백업하는 작업
## 특정 디렉토리 내의 모든 파일을 ZIP 형식으로 압축
## 이를 FTP 서버로 자동 전송하는 프로그램 작성

# 조건
## 1. static 디렉토리 내의 모든 파일을 순회하면서 Zip 파일로 압축
## 2. 압축된 파일의 이름에는 디렉터리 이름과 현재 날짜가 포함
## 3. 압축이 완료된 후, 생성된 ZIP 파일을 FTP 서버로 전송한다.
## 4. 네트워크 지연이나 파일 크깅 따른 전송 시간을 고려 / 적절한 타이밍에 프로그램이 실행

import ftplib
import os
import zipfile
from datetime import datetime

ftp = None

def connectFTP(host, id, password):
    global ftp
    hostname = host
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(id, password)
        print("FTP 연결 성공")
        return ftp
    except Exception as e:
        print("FTP 연결 실패:", e)
        ftp = None
        return False

def makeZip():
    nameDirect = 'static'
    file_path = os.path.join(os.getcwd(), nameDirect)

    if not os.path.exists(file_path):
        os.mkdir(file_path)
    
    zipName = f"{nameDirect}-{datetime.now().strftime('%Y-%m-%d')}.zip"

    with zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(nameDirect):
            for file in files:
                fpath = os.path.join(root, file)
                arcname = os.path.relpath(fpath, start=nameDirect)
                zipf.write(fpath, arcname)
    print(f"ZIP 파일 생성 완료: {zipName}")
    return zipName

def uploadFTP(zipname):
    try:
        with open(zipname, "rb") as file:
            ftp.storbinary(f"STOR {os.path.basename(zipname)}", file)
        print(f"FTP 업로드 완료: {zipname}")
    except Exception as e:
        print("FTP 업로드 실패:", e)

def runsAll():
    zipname = makeZip()          # ZIP 생성
    uploadFTP(zipname)