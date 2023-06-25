import requests

token = '6248460195:AAHGfOAzWV21IXwP4jEgxVntWPm5qE5EEpE'
chat_id=6120864080
bot_message="hello"

url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={bot_message}"

requests.get(url)