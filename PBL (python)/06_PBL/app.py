from flask import Flask
from flask import render_template, request, redirect, url_for
import ftplib
import schedule
import time
import threading

## function call
from functionCall import ftp
from functionCall import connectFTP, runsAll

app = Flask(__name__)

ftp = None

@app.route('/')
def start():
    return render_template('login.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    global ftp

    if request.method == 'POST': # POST 요청 처리
        ip = request.form['ip']
        userId = request.form['userId']
        password = request.form['password']

        ftp = connectFTP(ip, userId, password)
        print(ftp)
        
        if ftp:
            return redirect(url_for('ListFiles'))
        else:
           return render_template('login.html') 
    return render_template('login.html')

@app.route("/list")
def ListFiles():
    if ftp is None: 
        return redirect(url_for('login'))
    try:
        files = ftp.nlst() 
        return render_template('index.html', files=files)
    except Exception as error:
        return f"파일 목록 불러오기 실패 : {str(error)}"

def main():
    schedule.every().day.at("18:49").do(runsAll)
    while True:
        schedule.run_pending()
        time.sleep(1)

# thread 분리로 app 서버 + scheduler 사용
if __name__ == "__main__" :
    scheduler_thread = threading.Thread(target=main)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    app.run(debug=True)
