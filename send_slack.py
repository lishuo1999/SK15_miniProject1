from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests
import json

# Slack API 토큰 및 채널 정보
SLACK_API_TOKEN= "xoxe.xoxp-1-Mi0yLTU1OTE2OTQ5MzA0ODUtNTU4Nzk2MDU4NjQwNi01NjEyMzAwNzE2MDg0LTU2MjQyMDExNDAxNjEtOTRjYmVlZmI0MWQ1YTJkYjcxZmIyMGFiZWFkMmFlNGM5MDBkOGU1ZjNiMDEwOWM5NTJlM2Q4YzE2M2ZkMjQzYQ"
SLACK_CHANNEL = "#python_test01"

def sendSlackMessage(strText):
    # Slack 메시지 전송을 위한 Web API URL 및 데이터 설정
    slack_url = "https://hooks.slack.com/services/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"
    data = {"text":strText, "channel":SLACK_CHANNEL}
    headers = {"Content-type":"application/json"}

    # Slack에 메시지 전송 요청
    requests.post(slack_url, headers=headers, data=json.dumps(data))


def sendSlackFile(file_path):
    # Slack 파일 전송을 위한 WebClient 객체 생성
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        # Slack 파일 업로드 요청
        response2 = client.files_upload(
            channels=SLACK_CHANNEL,
            file=file_path,
            title=f"개인정보포함파일"
        )
        print(f"정상적으로 보냄")
    except SlackApiError as e:
        print(f"오류 발생 {e}")
    
def sendSlackMain():
    # Slack에 전송할 파일 경로
    output_path = "information.xlsx"
    sendSlackFile(output_path) # 파일 전송
    sendSlackMessage("개인정보가 포함된 파일입니다.")


