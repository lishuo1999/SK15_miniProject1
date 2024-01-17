# SSRLC 6조 미니 프로젝트

#### 프로젝트 개요 및 목표

이번 6조 프로젝트는 웹 홈페이지를 통해 업로드를 하여서, 주민등록번호나 이메일 등 개인정보가 포함되어 있는지 여부를 보안 담당자가 확인하고 신속한 조치가 가능하게 하여 개인정보보호 및 보안 강화, 하나씩 검사하는 번거로움을 줄이는 업무 효율성 향상, email과 slack메시지를 통해 팀원들과 즉각적으로 결과를 공유하여 팀 커뮤니케이션 강화의 목적이 있습니다.


#### 다음은 코드 설명입니다. 

###### app.py 코드 설명입니다.

1. 다음은 app.py 시작입니다.

```python
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
```

    시작단계에서 upload.html을 실행해서 업로드 할 홈페이지를 띄어줍니다.


2. 다음 함수는 email과 주민등록번호가 있는지 확인하게 됩니다.

   ```python
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
   ```


3. 파일 경로 저장

   ```python
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

   ```

    다음은 홈페이지에서 받은 파일들을 저장하기 위한 경로 지정입니다.

4. 개인정보 검출 전송

   ```python
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
   ```

   다음은 업로드된 파일에서 저장된 파일에서 검출된 개인정보들을 보안 담당자들에게 slack과 email로 보내는 코드입니다.  전송이 완료가 되면 check.html이 실행되게 됩니다.
6. 전송 성공 페이지 실행

   ```python
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
   ```

    slack이나 email로 전송이 완료되면 전송이 성공되었다는 페이지를 실행하게 됩니다.


###### upload.html 코드 설명

1. title및 스타일 설명

   "`<head>`"안으로 들어가게 됩니다.

   ```html
   <meta charset="UTF-8">
       <title>파일 업로드 페이지</title>
       <style>
           h1 {
               padding: 10px;
               background-color: #FFAAAF;
               color: #FF1493;
               font-style: italic;
               text-align: center;
           }
           legend {
               border: 5px double black;
               padding: 5px;
               background-color: #FFAAAF;
               text-align: center;
           }
       </style>
   ```

    페이지 제목으로 파일 업로드 페이지가 나타나게 되고, h1과 legend 부분의 style을 정하기 위하여 만들었습니다.

2. 프로그램 실행을 위한 function입니다.

   "`<head>`"안으로 들어가게 됩니다.

```python
<script>
        let fileList = []; // Temporary list to store selected files

        function displayFileNames() {
            const fileInput = document.getElementById('file');
            const fileListElement = document.getElementById('file-list');
            fileListElement.innerHTML = '';
            for (const file of fileInput.files) {
                fileList.push({ file, timestamp: getClock() }); // Store selected file and timestamp in the list
                const listItem = document.createElement('li');
                listItem.textContent = `${file.name} - ${getClock()}`;
                fileListElement.appendChild(listItem);
            }
            showUploadCompleteAlert();
        }

        function uploadFiles() {
            // 여기에서 파일 업로드 기능을 구현
            // "fileList" 배열을 사용하여 선택한 파일 목록에 접근 가능
            if (fileList.length === 0) {
                alert("No files selected for upload.");
                return;
            }
            // Simulate the upload process by displaying the file names and upload dates in the second fieldset
            const fileListElement = document.getElementById('file-list');
            fileListElement.innerHTML = '';
            for (const { file, timestamp } of fileList) {
                const listItem = document.createElement('li');
                listItem.textContent = `${file.name}  (Uploaded Date : ${timestamp})`;
                fileListElement.appendChild(listItem);
            }
        }
      
        function showUploadCompleteAlert(){
            alert("업로드 완료!");
        }

        function getClock() {
            //시간 및 날짜 구현을 위한 함수
            const date = new Date();
            const year = String(date.getFullYear());
            const month = String(date.getMonth() + 1).padStart(2, "0");
            const day = String(date.getDate()).padStart(2, "0");
            const hours = String(date.getHours()).padStart(2, "0");
            const min = String(date.getMinutes()).padStart(2, "0");
            const sec = String(date.getSeconds()).padStart(2, "0");
            return `${year}/${month}/${day} ${hours}:${min}:${sec}`;
        }

    </script>
```

실행을 하기 위한 함수 4개를 만들었습니다.

filelist로 저장할 파일들을 저장하기 위한 리스트를 만듭니다.

displayFileNames() 함수를 만들어  filelist함수에 저장된 파일들을 출력하기 위한 함수를 만들었습니다.

uploadFiles() 함수를 만들어 실질적으로 파일들을 업로드 하기 위한 함수를 만들었습니다. 

showUploadCompleteAlert() 함수를 만들어 업로드가 완료되면 업로드 완료 웹 메시지가 출력하게 됩니다.

마지막으로 getClock() 함수를 만들어 업로드된 파일들의 업로드 시간을 출력하게 됩니다. 


이제부터는 "`<body>`"로 들어가는 코드로, 실질적인 페이지를 구형하기 되는 코드입니다. 

3. 헤드 코드

   ```python
   <h1>
           <div id="logo">
               <a><h1>FILE UPLOAD PAGE</h1></a>
           </div>
       </h1>
   ```

페이지의 상단에 해드파일로, FILE UPLOAD PAGE를 출력하게 됩니다. h1의 스타일은 `<head> `세션에서 저장된 h1 스타일이 적용되게 됩니다. 

4. 홈페이지 메인
