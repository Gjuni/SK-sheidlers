from flask import Flask
from flask import render_template ## 포트포워딩 시킴. 해당 templates/'file_name.html' 로 이동 시킨다.
from flask import redirect
from flask import request
import feedparser

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/rss", methods=['GET', 'POST'])
def rss():
    rss_url = request.form['rss_url']
    feed = feedparser.parse(rss_url)
    return render_template('rss.html', feed=feed)
    

if __name__ == '__main__':  # app 실행
    app.run(debug=True)     # 개발자 모드로 실행. 외부 실행 X localhost로만 실행

## https://www.dailysecu.com/rss/S1N2.xml