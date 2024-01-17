from flask import Flask, render_template, request
import os
import re
import datetime
from send_slack import sendSlackMain
from mailsend import mail_sender
from make_excel import makeExcel

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('upload.html')

# Email 검사
# 정규표현식을 사용해 Email이 포함되었는지 확인 후 boolean 형식으로 True나 False를 반환하는 함수
def check_email(content):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return bool(re.findall(email_pattern, content)) 

# 주민등록번호 검사
# 정규표현식을 사용해 주민등록번호 포함되었는지 확인 후 boolean 형식으로 True나 False를 반환하는 함수
def check_jumin(content):
    jumin_pattern = r"\b\d{6}-\d{7}\b"
    return bool(re.findall(jumin_pattern, content))

@app.route('/result', methods=['POST'])
def result():
    # 파일 업로드 경로
    upload_path = "uploads"
    # 업로드 한 파일을 저장하기 위한 리스트
    uploaded_files = []  
    # request 모듈을 사용해 여러 개의 파일을 업로드 한 리스트를 만들어 files에 저장
    files = request.files.getlist("file[]")
    # 업로드 한 파일들 upload폴더로 저장
    for file in files:
        file.save(os.path.join('uploads', file.filename))

    # upload 파일 경로에 있는 file들을 반복
    for file in os.listdir(upload_path):
        # 각 파일마다 파일의 경로 지정
        file_path = os.path.join(upload_path, file)

        # 해당 파일을 ISO-8859-1 형식, 일기 권한으로 읽어 f 라 명칭
        with open(file_path, "r", encoding="ISO-8859-1") as f:
            # 해당 파일의 컨텐츠를 불러옴
            content = f.read()
            # 컨텐츠에 이메일 형식이 있으면 True 값을 반환하는 함수 호출
            email = check_email(content)
            # 컨텐츠에 주민등록번호가 있으면 True 값을 반환하는 함수 호출
            jumin = check_jumin(content)

        # 파일의 생성시간을 받아와 저장
        ctime_datetime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        uploaded_files.append((file, os.path.getsize(file_path), ctime_datetime.strftime('%Y-%m-%d %H:%M:%S'), email, jumin))

    makeExcel(uploaded_files)
    return render_template("result.html", results=uploaded_files)


# slack 전송
@app.route('/sendSlack', methods=['POST'])
def sendSlack():
    #print(request.args.get('slack'))
    sendSlackMain()
    check()
    return render_template('check.html')
    # sendSlackMain()로 함수 실행 가능


# 메일전송
@app.route('/sendMail', methods=['POST'])
def sendMail():
    mail_sender()
    check()
    return render_template('check.html')

    
# 전송 성공 페이지
@app.route('/check')
def check():
    #uploads 폴더 초기화
    upload_path = 'uploads'
    for file in os.listdir(upload_path):
        file_path = os.path.join(upload_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)
