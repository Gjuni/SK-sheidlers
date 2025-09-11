## https://www.malware-traffic-analysis.net/2023/index.html 를 크롤링 해서
## 1. 제목 주소를 가져오시오.
## 2. 링크 정보를 전체 URL 형식으로 출력하세요. (https://www.malware-traffic-analysis.net 로 시작) 절대경로로 바꿀 것
## 3. 결과 값을 txt 파일로 저장하세요.!!

import requests
from bs4 import BeautifulSoup

year = int(input("검색할 연도 입력 2013 ~ 2025: "))

switch = True
while(switch):
    if((int(year) >= 2013) and (int(year) <= 2025)):
        switch = False
    else :
        year = input("년도는 2013 ~ 2025년까지입니다 : ")
        switch = True

url = f"https://www.malware-traffic-analysis.net/{year}/index.html"

header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'}

r = requests.get(url, header_info)

soup = BeautifulSoup(r.text, 'html.parser')

content = soup.select('#main_content > div.content > ul > li > a.main_menu')
date = soup.select('#main_content > div.content > ul > li > a.list_header')
for i,j in zip(date, content) :
    print(f"date : {i.text}, name : {j.text}")