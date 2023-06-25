import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_json('tqa_dataset.json')
    return df

model = cached_model()
df = get_dataset()

st.header('도서 퀴즈 챗봇')
if 'generated' not in st.session_state: #st.session_state는 세부사항을 담는 공간
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'context' not in st.session_state:
    st.session_state['context'] = []
with st.form('form', clear_on_submit=True): #사용자가 입력하는 칸
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze()) #유사도를 비교해주는 열
    answers = df.loc[df['distance'].idxmax()] #답변

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answers['answers'])
    st.session_state.context.append(answers['context'])

    for i in range(len(st.session_state['past'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot') #message함수로 내용 출력
        message(st.session_state['context'][i], key=str(i) + '_botContext') #message함수로 세부 내용 출력