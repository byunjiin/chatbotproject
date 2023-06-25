import requests
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

token = '6248460195:AAHGfOAzWV21IXwP4jEgxVntWPm5qE5EEpE'
chat_id=6120864080

def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

def get_dataset():
    df = pd.read_csv('W_1.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

#cach해주는 함수 만들기
model = cached_model()
df = get_dataset()

#내용을 주고 받을때 마지막 대화에서부터 새로 추가된것만 반영
last_update_id = None
while True: #while문으로 반복하며 갱신
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    if last_update_id: #가져왔을때, 마지막에서 추가된게 있을때만 가져옴
        url += f"?offset={last_update_id + 1}"
    response = requests.get(url)
    if response.status_code != 200: #200=리퀘스트 요청이 정상처리 (404=애러)
        continue #정상일 경우 아래코드, 200이면 continue로 다시 맨 위로
    data = response.json()

    for update in data["result"]:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        update_id = update["update_id"]

        last_update_id = update_id #갱신

        embedding = model.encode(text) #유저가 입력한걸 받아옴

        #문장간의 유사도 분석
        df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
        answer = df.loc[df['distance'].idxmax()]
        bot_message = answer['챗봇']

        #터미널 창에서 볼 수 있게 print
        print(answer['distance'])
        print(answer['유저'])
        print(answer['챗봇'])

        url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={bot_message}"

        requests.get(url)