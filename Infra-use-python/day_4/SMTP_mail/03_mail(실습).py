import smtplib
from email.mime.multipart import MIMEMultipart ## 첨부파일 전송 할때
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication ## 첨부파일 전송 시 MIMEApplication으로 폼을 바꿔서 전송함.
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
import os

load_dotenv()
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "kmj06178@gmail.com"

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login(send_email,send_pwd)
  
text = f"탐지라인:"

msg = MIMEMultipart()
msg['Subject'] = f"루키즈 실습 번역하기:"  
msg['From'] = send_email          
msg['To'] = recv_email

initial_text ="<b>번역하였습니다.</b><br><br>--- 번역된 파일 내용 ---<br>"

## 첨부파일
etc_file_path = r'uploads/1.txt'
with open(etc_file_path, 'r', encoding='utf-8') as f : # 텍스트 모드로 파일을 읽습니다.
    original_content = "".join(f.readlines()) ## 파일 라인 합치기
    translated_content = GoogleTranslator(source='ko', target='en').translate(original_content)

# HTML 형식으로 본문을 구성합니다.
html_body = f"{initial_text}{translated_content.replace('\n', '<br>')}"
contentPart = MIMEText(html_body, 'html') # HTML 형식으로 MIMEText를 생성합니다.
msg.attach(contentPart)

smtp.sendmail(send_email,recv_email,msg.as_string() )
smtp.quit()