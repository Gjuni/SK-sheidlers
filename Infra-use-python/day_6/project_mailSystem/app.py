from flask import Flask
# 1. user.Controller 파일에서 생성한 user_bp 블루프린트 객체를 가져옵니다.
from user.userController import user
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(user)
        

if __name__ == "__main__":
    app.run(debug=True)