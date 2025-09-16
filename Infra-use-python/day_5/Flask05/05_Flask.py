from flask import Flask, render_template, request, send_file
import os
from datetime import datetime
import zipfile

## streamlit 이라는 웹 서비스 있음. 데이터 분석 및 시각화에 탁월함. 자동화 할 때 사용하면 정말 편해짐
## 위젯 형식으로 돌아감. 파이썬으로 자동화 사용할 시 사용하면 좋다.


UPLOAD_PATH = 'uploads'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def list():
    files = []

    for file in os.listdir(UPLOAD_PATH): # 폴더이냐 디렉토리냐 확인 하고 디렉토리면 그 안에 세부 탐색 시 listdir 사용하는게 편하다.
        # 속성 정보를 알아야한다. 파일에 size, 정보 파일 생성 ctime -> data를 묶어서 전송
        file_path = os.path.join(UPLOAD_PATH, file)
        file_size = os.path.getsize(file_path)
        file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d, %H:%M:%S') # 접근하는 시간
            ## fromtimestamp는 컴퓨터가 1970년부터 계산한 초 단위를 사람이 읽을 수 있게 만든 라이브러리
            ## strftime은 원하는 형태로 날짜를 만듬.

        files.append((file, file_path, file_size, file_ctime))

    return render_template('list.html', files=files)

@app.route('/compress', methods=['GET', 'POST'])
def compress():
    files = request.form.getlist("files") # getlist는 파일을 리스트 형태로 받겠다는 선언문. get("file")로 단일 객체 하나만 받을 수 있지만 files가 list의 경우 getlist로 받아야한다.
    zip_path = os.path.join(UPLOAD_PATH, "compress.zip")

    with zipfile.ZipFile(zip_path, "w") as zip_file:
         for file in files:
              file_path = os.path.join(UPLOAD_PATH, file)
              zip_file.write(file_path, file)

    return send_file(zip_path, as_attachment=True)
    
if __name__ == "__main__":
    app.run(debug=True)