import streamlit as st #streamlit = 파이썬코드를 시각화
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask') #언어변경
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('hospital-dataset.csv') #여기에 데이터셋을 넣음
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('병원챗봇') #제목

if 'generated' not in st.session_state:
    st.session_state['generated'] = [] #초기화

if 'past' not in st.session_state:
    st.session_state['past'] = [] #초기화

with st.form('form', clear_on_submit=True) : #with문은 안에 있는 블럭을 실행하기 전에 요소들을 초기화하고, 종료후에 다시 초기화해줌
    user_input = st.text_input('당신: ','') #입력
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding],[x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])

for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i],is_user=True, key=str(i)+'_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i],key=str(i)+'_bot')