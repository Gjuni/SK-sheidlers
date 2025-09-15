from flask import Flask
from flask import render_template
from flask import request
import os
from deep_translator import GoogleTranslator

app = Flask(__name__) # Flask 실행

@app.route('/')
### '/' router로 가게 된다면 index 함수를 실행해라
def index():
    ### templates/index.html 파일을 불러와라
    return render_template("index.html") 


## router 지정 - method는 Get과 POST (default : get)
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files["file"] ## file을 받을 때 request를 사용

    # uploads 폴더가 없으면 생성
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # 경로 지정
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    content = ""
    translated_content = ""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # deep-translator는 긴 텍스트도 한 번에 번역할 수 있습니다.
    # 텍스트가 매우 길 경우, API 제한을 피하기 위해 아래처럼 줄 단위로 번역하는 것이 안정적일 수 있습니다.
    translated_lines = []
    for line in content.splitlines():
        translated_line = GoogleTranslator(source='ko', target='en').translate(line)
        translated_lines.append(translated_line)
    translated_content = '\n'.join(translated_lines)
    
    return render_template('next.html', file_content=content, file_content2=translated_content)
            
# 어플리케이션 start
if (__name__ == "__main__"):
    app.run(debug=True)