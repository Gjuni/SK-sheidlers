from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <div data-role="page" data-last-modified="2022-01-01" data-foo="value">This is a div with data attributes.</div>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2" data-info="more info">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3" data-info="even more info">Tillie abcd</a>
    ; and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

### find = 1개의 결과만
### find_all = 여러 정보를 가져옴


soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

print(soup.title) # title tag만 가져옴
print(soup.title.string) ## Tag를 제거하고 내용만 가져오게 하는 방법

print(soup.p) # p Tag 한개만 나온다. find_all을 사용해야 전부 가져옴

#class 정보 가져오는 방법
print(soup.p['class']) # title 정보를 가져옴. p tag의 class를 가져옴

# findAll - list 방식으로 빼온다.
# 각 원소마다 빼오기 -> for 문
print(soup.find_all('a'))
soup_find_all = soup.find_all('a')

for link in soup_find_all :
    print(link)
    print(link.get('href'))