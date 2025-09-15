## 웹 스크래핑을 통한 보안 정보 자동화 시스템 프로그램 개발

# 조건
## 1. https://www.malware-traffic-analysis.net/2024/index.html (스크래핑 할 것)
## 2. 웹 사이트에서 최신 보안 동향 정보를 정기적으로 스크래핑할 것
## 3. 이를 엑셀 파일에 정리하여 관련 담당자에게 자동으로 이메일로 전송하는 시스템 개발
## 4. 엑셀 파일의 첫 번째 열에는 제목, 두 번째 열에는 URL 링크가 포함되어야함.

from bs4 import BeautifulSoup
import requests
import schedule
import time
import os
from datetime import datetime
from openpyxl import Workbook
import smtplib # 메일 전송하는 라이브러리
# 파일 처리 라이브러리
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

## 전역 변수 선언
scrap_url = "https://www.malware-traffic-analysis.net/2024/index.html"
titles = []
links = []
now_day = ""
file_path=""

# dotenv 선언 아숩다..
REPORT_DIR = "report"
EMAIL="hashsha128@gmail.com"
MAILPASSWORD="ijeiqcgjrgcpeywr"

## 스크래핑 저장 폴더 생성
def makedir():
    os.makedirs(REPORT_DIR, exist_ok=True)

## 해당 URL 스크랩 내용 List에 저장
def scrapping():
    global titles
    global links

    header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'}
    req = requests.get(scrap_url, headers=header_info, verify=False) ## Web 상에 request를 보내는 것
    soup = BeautifulSoup(req.text, 'html.parser')

    tags = soup.select('#main_content > div > ul > li > a.main_menu')

    for tag in tags:
        link_text = tag.text # text로 받아옴. -> tag 지움. -> 제목의 값
        link_href = f"{scrap_url}/{tag.get('href')}" # HTML tag의 href의 값을 받아온다. -> Link 값
        titles.append(link_text)
        links.append(link_href)
    

## 워크북 생성 및 데이터 삽입
def workbook():
    global now_day
    global file_path
    now_day = datetime.now().strftime("%Y-%m-%d") # 날자 기준으로 데이터 전송
    
    wb = Workbook()
    ws = wb.active
    ws.title = f"{now_day}_malware_Report" # 시트 이름 변경

    header = ['Title', 'Link']
    ws.append(header)

    for i in range(len(titles)):
        ws.append([titles[i], links[i]])

    file_path = os.path.join(REPORT_DIR, f"{now_day}_malware_Report.xlsx") # 지정된 디렉토리로 파일 이름 지정
    wb.save(file_path)

## 메일로 전송
def sendMail():
    # 메일 객체 생성
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = "kmj06178@gmail.com" ## 커스텀 가능
    msg['Subject'] = f"{now_day}일자 report 송부합니다"

    ## 메일 본문 추가
    body = f"{now_day}일자 malware Report입니다."
    msg.attach(MIMEText(body, 'plain')) # 본문 콘텐츠 타입 = plain

    with open(file_path, "rb") as file : ## r을 사용시 바이너리 파일인 엑셀을 제대로 읽지 못 하였음
        data = MIMEBase("application", "MIME")
        data.set_payload(file.read())

    encoders.encode_base64(data)

    data.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(file_path)}",
    )

    msg.attach(data)

    ## STMP 전송
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(EMAIL, MAILPASSWORD)
    session.sendmail(EMAIL, "kmj06178@gmail.com", msg.as_string())
    print("메일 전송 완료")
    session.quit()
    

## schedule을 위한 실행 함수 모음
def runsAll():
    makedir()
    scrapping()
    workbook()
    sendMail()

def main():
    schedule.every().day.at("18:36").do(runsAll)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if (__name__ == "__main__"):
    main()