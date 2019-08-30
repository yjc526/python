import requests
from decouple import config

base  = "https://api.telegram.org"
token = config("TOKEN")

url = f"{base}/bot{token}"


lastMsgCnt = 0

while True:
    res = requests.get(url+"/getUpdates")
    data = res.json()

    currentMsgCnt = len(data["result"])

    if lastMsgCnt<currentMsgCnt:
        id = data["result"][currentMsgCnt-1]["message"]["chat"]["id"]
        text = data["result"][currentMsgCnt-1]["message"]["text"]
        requests.get(f"{url}/sendMessage?text={text}에 대한 답변입니다.&chat_id={id}")
        lastMsgCnt = currentMsgCnt

