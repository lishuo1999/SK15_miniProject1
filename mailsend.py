import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
from dotenv import load_dotenv
import os
from datetime import datetime

def mail_sender():
     # .env 파일에서 환경 변수 로드
    load_dotenv()
    SECRET_ID = os.getenv("ID")
    SECRET_PASS = os.getenv("PASS")
    filepath = 'information.xlsx'
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # SMTP 서버에 연결
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()
    
    # SMTP 서버에 로그인
    smtp.login(SECRET_ID,SECRET_PASS)

    myemail = 'sk15project6@naver.com'
    youremail = 'sk15project6@naver.com'

    # 이메일 메시지 객체 생성
    msg = MIMEMultipart()

    msg['Subject'] ="[중요] 파일 내 개인정보 탐지"
    msg['From'] = myemail
    msg['To'] = youremail

    # HTML 형식의 이메일 본문 작성
    text = """
    <html>
    <body>
    <h1 style="color:red;">
    {}<br>
    업로드 하신 파일 안에서 개인정보가 탐지되었습니다. 
    </h1>
    </body>
    </html>
    """.format(now)

    contentPart = MIMEText(text, 'html') 
    msg.attach(contentPart) 

    # 개인정보가 포함된 파일을 이메일에 첨부
    with open(filepath, 'rb') as f : 
            etc_part = MIMEApplication( f.read() )
            etc_part.add_header('Content-Disposition','attachment', filename=filepath)
            msg.attach(etc_part)

    # 이메일 송신
    smtp.sendmail( myemail,youremail,msg.as_string() )
    smtp.quit()

if __name__ == '__main__':
    mail_sender()
