## FTP 서비스에 수시로 파일들이 저장되고 처리되는데
## 이를 자동으로 목록화 해주는 작업을 자동화 할 게획

# 조건
# index.html (FTP 파일 목록) / login.html (FPT 접속 <ip, userId, password>)
## 1. Flask 웹 프레임워크를 사용하여 서버 파일 목록을 불러와 웹 페이지에 출력
## 2. login 기능을 Flask에서 불러올 수 있도록 설정
## 3. 로그인 후 서버의 파일 목록을 볼 수 있는 기능을 포함해야함.

# 기능 구현
## POST/ login (IP & userId & Password 전달)
## GET/ list (FTP 목록 listUp)

from flask import Flask, request, render_template, redirect, url_for
import ftplib

## 전역 변수 선언
ftp = None

app = Flask(__name__)

## Home(health Check로 많이 쓰임)
@app.route('/')
def healthCheck():
    return redirect(url_for('login'))

## login Router
@app.route('/login', methods=['GET', 'POST'])
def login():
    global ftp
    if(request.method == 'POST'):
        ip = request.form['ip']
        userId = request.form['userId']
        password = request.form['password']

        try:
            ftp = ftplib.FTP(ip)
            ftp.login(userId, password)
            return redirect(url_for('ListFiles'))
        except Exception as error:
            return f"로그인 실패 : {str(error)}"
    return render_template('login.html')

## File List Router
@app.get('/list')
def ListFiles():
    global ftp
    if ftp is None:
        return redirect(url_for('login'))
    else :
        try:
            files = ftp.nlst() # 현재 디렉토리에 저장된 파일들을 불러옴.
            return render_template('index.html', files=files)
        except Exception as error:
            return f"파일 목록 불러오기 실패 : {str(error)}"


if(__name__ == '__main__'):
    app.run(debug=True)