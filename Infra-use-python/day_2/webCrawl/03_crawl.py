import requests
from bs4 import BeautifulSoup

query = input("쿼리값 입력하시오 : ")

url = f"https://kin.naver.com/search/list.naver?query={query}"

header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'} ## user Agent가 없으면 비정상으로 출력됨

r = requests.get(url, headers=header_info)

soup = BeautifulSoup(r.text, 'html.parser') ## r의 text파일의 내용을 가져오겠다. 어떻게 가져오냐? html.parser

## 특정 값을 입력하게 되면 1번째 Page 제목, 날짜들을 가져오게 해라
contents  =soup.select('#s_content > div.section > ul > li > dl > dt > a')
dates = soup.select('#s_content > div.section > ul > li > dl > dd.txt_inline')

for content in contents:
    print(f"질문 : {content.text}")

## List 형식을 데이터를 묶어서 사용하는 것
for content, date in zip(contents, dates) :
    print(f"질문 : {content.text}, 날짜 : {date.text}")