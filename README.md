# SK15_Team6
SK쉴더스 루키즈 15기 미니프로젝트
## 개요
- 주제 : ```슬랙 API 활용한 개인정보 포함 여부 검사 서비스 개발```
- 진행 기간 : ```2023.07.20 ~ 2023.07.21```
- 참여 인원 : ```6명```
- 역할 : ```result 페이지 개발``` 

</br>

## 기술 스택
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=CSS3&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white" /> <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=Flask&logoColor=white" /> <img src="https://img.shields.io/badge/Slack-4A154B?style=flat&logo=Slack&logoColor=white" /> <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white" />


</br>

## 프로젝트 소개
- Email이나 주민등록번호와 같은 중요 개인정보를 포함한 파일 여부를 자동으로 검사하는 웹 서비스 제공
- 본 프로젝트에서 파이썬 웹 프레임워크인 Flask를 사용하여 API 서버 역할로 사용
- 슬랙 API를 활용해 검사 결과 메시지를 담당자에게 자동 전송 기능 제공




</br>

## 서비스 주요 특징
- 사용자는 중요 개인정보 포함 여부 확인하고자 하는 파일을 웹 페이지에 업로드
- 중요 개인정보 포함 검사 내용은 Email과 주민등록번호 포함 여부 검사
- 검사 결과는 이메일 및 슬랙 중 선택하여 수신 가능하며, 중요 개인정보가 확인되면 해당 파일과 함께 담당자에게 전송
- 중요 개인정보 포함 여부 검사결과를 엑셀 파일로 저장하여 가독성 강화

</br>

## 담당 역할 및 학습 내용
- 중요 개인정보 포함 여부 검사결과 페이지 개발
- 슬랙 API 활용한 메시지 전송 기능 학습
- 파이썬 smtplib 라이브러리 활용해 이메일 전송 기능 학습
