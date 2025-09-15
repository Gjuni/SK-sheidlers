## 1. RSS 서비스에서 list.txt 파일의 정보를 수집한다.
## 2. Feedparser를 이용해서 정보를 수집
## 3. 수집된 정보를 xlsx 파일에 리스트별로 지정(3개 파일)한다.
## 4. uploads 폴더에 3개의 xlsx 파일이 저장이 될 것이다.
## 5. zip 파일을 FTP에서 전송한다.

import feedparser
import zipfile
import os
import ftplib
from openpyxl import Workbook

RESULT_DIR = "results"

if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)

## 파일 이름 정의
file_name = 'list.txt'

## FTP host 정의 및 접속
hostname = "192.168.38.129"
ftp = ftplib.FTP(hostname)
ftp.login('msfadmin','msfadmin')

## feedparser
with open(file_name, 'r', encoding='utf-8') as file:
    urls = file.readlines()

    for index, url in enumerate(urls):
        titles= []
        descriptions = []
        links = []

        fp = feedparser.parse(url)

        for entry in fp.entries:
            titles.append(entry.title)
            descriptions.append(entry.description)
            links.append(entry.link)
        
        ## Workbook 정의
        wb = Workbook()
        ws = wb.active
        ws.title = f"{index+1}번째 Data"

        header = ['Title', 'Description', 'link']

        for i in range(len(titles)):
            ws.append([titles[i], descriptions[i], links[i]])

        # 엑셀 파일로 저장.
        file_path = os.path.join(RESULT_DIR, f'{index+1}_result_xlsx')
        wb.save(file_path)

# 결과 값을 zip파일로 변환
zip_file = zipfile.ZipFile("result.zip", "w")

for root, dirs, files in os.walk(RESULT_DIR):
    for file in files :
        zip_file.write(os.path.join(root, file)) # root 파일을 순차 탐색하면서 zip 폴더에 write함.

zip_file.close()

## FTP 서버 결과값 전송
ftp.retrlines('LIST')

with open("result.zip", "rb") as f:
    ftp.storbinary(f"STOR result.zip", f)

print(f"현재 작업 디렉토리 : {ftp.pwd()}")
ftp.retrlines('LIST')
ftp.quit()