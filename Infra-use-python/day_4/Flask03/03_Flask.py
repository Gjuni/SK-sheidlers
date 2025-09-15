from docx import Document
from docx2pdf import convert
from flask import Flask
from flask import render_template, request, send_file

app = Flask(__name__)

doc = Document('template.docx') ## docx 파일 불러오기
name =""
course=""
date=""

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods = ['GET', 'POST'])
def upload():
    global name
    global course
    global date

    name = request.form['NAME']
    course = request.form['COURSE']
    date = request.form['DATE']

    for paragraph in doc.paragraphs: ## 각 문구(객체)별로 가져오는 것
        comment = paragraph.text
        # print(paragraph.text) ## text 해야 텍스트를 잘 뽑아옴.

        ## 해당 text에 맞는 값들 변경
        if 'NAME' in comment:
            paragraph.text = paragraph.text.replace('NAME', name)
        if 'COURSE' in comment:
            paragraph.text = paragraph.text.replace('NAME', course)
        if 'DATE' in comment:
            paragraph.text = paragraph.text.replace('DATE', date)
    
    doc_name = f"{name}_{course}_수료증.docx"
    pdf_name = f"{name}_{course}_수료증.pdf"
    doc.save(doc_name)
    ## PDF 파일 변환
    convert(doc_name, pdf_name)
    return render_template('result.html')


@app.route('/result', methods=['GET'])
def result():
    return send_file(f"{name}_{course}_수료증.pdf", as_attachment=True)


if __name__ == "__main__" :
    app.run(debug=True)