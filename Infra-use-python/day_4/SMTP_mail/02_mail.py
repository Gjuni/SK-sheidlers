import smtplib
from email.mime.multipart import MIMEMultipart ## 첨부파일 전송 할때
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication ## 첨부파일 전송 시 MIMEApplication으로 폼을 바꿔서 전송함.
from dotenv import load_dotenv
import os

load_dotenv()
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "yours@naver.com"

smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login(send_email,send_pwd)
  
text = f"탐지라인:"

msg = MIMEMultipart()
msg['Subject'] = f"모니터 탐지:"  
msg['From'] = send_email          
msg['To'] = recv_email

text ="<b>탐지되었습니다.</b>"

## 본문
contentPart = MIMEText(text) 
msg.attach(contentPart) 

## 첨부파일
etc_file_path = r'uploads/1.txt'
with open(etc_file_path, 'rb') as f : # 읽어서 보냄. 파일을 바이너리 형태로 읽음.
    etc_part = MIMEApplication( f.read() )  ## 파일을 읽은 후 MIME Application 형태로 변환
    etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path) # add_header에서 attachment(첨부파일)로 붙혀서 전송하겠다.
    msg.attach(etc_part)

smtp.sendmail(send_email,recv_email,msg.as_string() )
smtp.quit()