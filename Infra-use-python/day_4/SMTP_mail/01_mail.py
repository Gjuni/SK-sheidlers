#uploads 폴더의 디렉터리 정보를 수집
#파일 확장자가 txt 인 것을 리스트화
#txt 파일을 열어서 출력

import os
import re
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

def mail_sender(file_path, line):
    load_dotenv()
    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")
    recv_email = "boanproject1234@naver.com"

    smtp_name = "smtp.naver.com"
    smtp_port = 587              

    text = f"중요 정보 탐지 {file_path} : 라인 {line}"

    msg = MIMEText(text, 'plain', 'utf-8') 
    msg['Subject'] = f"{file_path} 내 중요 정보 탐지"  
    msg['From'] = send_email          
    msg['To'] = recv_email            

    email_string = msg.as_string()
    print(email_string)

    s = smtplib.SMTP(smtp_name, smtp_port)
    s.starttls()
    s.login(send_email, send_pwd)
    s.sendmail(send_email, recv_email, email_string)
    s.quit()


dir_path = "uploads"
all_files = os.listdir(dir_path)

txt_files = []

for file in all_files:
    if file.endswith(".txt"):
        txt_files.append(file)

# 1.txt, 2.txt  /uploads/1.txt
for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line.startswith("#") or line.startswith("//"):
                print(f"주석 {file_path} {index+1}라인: 탐지: {line.strip()}")
                mail_sender(file_path, line)
            if re.search(r'\d{6}\s*[-]\s*\d{7}', line):
                print(f"주민번호 {file_path} {index+1}라인: 탐지: {line.strip()}")
                mail_sender(file_path, line)