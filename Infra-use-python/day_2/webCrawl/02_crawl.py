import requests
from bs4 import BeautifulSoup

url = "https://zdnet.co.kr/"

header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'} ## user Agent가 없으면 비정상으로 출력됨

r = requests.get(url, headers=header_info)

soup = BeautifulSoup(r.text, 'html.parser') ## r의 text파일의 내용을 가져오겠다. 어떻게 가져오냐? html.parser

## Select_one을 사용하는 이유는 CSS에서 지원하는 값이 존재하기 때문 (세부적인 값을 필터링해서 가져오기)
links = soup.select("body > div.contentWrapper > div:nth-child(1) > div.left_cont > div.news1_box > div.news_list > div:nth-child(1) > div.assetText > a > h4") #div:nth-chile(1)에서 nth값을 지우면 div 전체를 다 가져옴. 근데 우리는 세부값이 필요하기 때문에 지우면 안됨
# CSS를 많이 사용하게 되는데 기존에 있던 Find와 비교했을 때 쉽게 만들게 된 것

for link in links :
    print(link.string)