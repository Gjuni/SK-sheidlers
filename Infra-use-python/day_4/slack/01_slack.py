from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

load_dotenv()

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

def send_message(channel, text):
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_API_TOKEN)
    
    try:
        # 채널에 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        # 응답 출력
        print("Message sent successfully:", response["message"]["text"])
    except SlackApiError as e:
        # 에러 처리
        print("Error sending message:", e.response["error"])

# 메시지 전송 함수 호출
send_message(SLACK_CHANNEL, "Hello, this is a test message from Slack API!")



def upload_file(channel, file_path, message):
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_API_TOKEN)
    
    try:
        # 파일을 Slack 채널에 업로드하고, 해당 파일에 메시지를 추가합니다.
        response = client.files_upload_v2(
            channel=channel, 
            file=file_path,
            initial_comment=message
        )
        # 업로드 성공 메시지 출력
        print("File uploaded successfully:", response["file"]["name"])
    except SlackApiError as e:
        # 에러 처리
        print("Error uploading file:", e.response["error"])

# 파일 업로드 및 메시지 전송 함수 호출
upload_file(SLACK_CHANNEL, "malwares.txt", "Here is the file you requested!")