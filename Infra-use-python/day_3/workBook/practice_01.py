## 1. RSS 서비스에서 list.txt 파일의 정보를 수집한다.
## 2. Feedparser를 이용해서 정보를 수집
## 3. 수집된 정보를 xlsx 파일에 리스트별로 지정(3개 파일)한다.
## 4. uploads 폴더에 3개의 xlsx 파일이 저장이 될 것이다.
## 5. zip 파일을 FTP에서 전송한다.

import feedparser
import zipfile
import os
import ftplib
from openpyxl import load_workbook
from openpyxl import Workbook

## 파일 이름 정의
file_name = 'list.txt'

## FTP host 정의 및 접속
hostname = "192.168.38.129"
ftp = ftplib.FTP(hostname)
ftp.login('msfadmin','msfadmin')

## feedparser
with open(file_name, 'r', encoding='utf-8') as urls:
    for url in urls:

        title= []
        decrition = []
        link = []

        ## Workbook 정의
        wb = Workbook()
        ws = wb.active
    
        fp = feedparser.parse(url)

        for entry in fp.entries:
            title.append(entry.title)
            decrition.append(entry.description)
            link.append(entry.link)
            




        
