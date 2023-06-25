import requests
import json

token = '6248460195:AAHGfOAzWV21IXwP4jEgxVntWPm5qE5EEpE'
chat_id=6120864080
bot_message="hello"

url=f"https://api.telegram.org/bot{token}/getUpdates"

data = requests.get(url).json()

print(url)

with open('chat.json', 'w', encoding='utf-8') as file: #w=쓰기모드 <새로운 파일 만들기>
    json.dump(data, file, indent="\t", ensure_ascii=False) #dump=기존의것을 버리고 새로작성