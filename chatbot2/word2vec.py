from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

def read_review_data(filename): 
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in #split()=괄호 안 문자기준으로 나눠짐(여기에선 tap)
f.read().splitlines()]
        data = data[1:] #0번째 주소엔 데이터명이므로 제외
    return data

start = time.time() #시작하는시간

print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./ratings.txt')
print(len(review_data))
print('1) 말뭉치 데이터 읽기 완료: ', time.time() - start) #현재시간-시작시간=걸린시간

print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료: ', time.time() - start)#현재시간-시작시간=걸린시간

print('3) word2vec 모델 학습 시작')
model = Word2Vec(sentences=docs, vector_size=200, window=4, min_count=2, sg=1) 
#vector_size=데이터몇(200)개, window=선택한 단어 기준으로 몇(4)개의 단어를 더 추측할지, min_count=최소 몇(2)번이상나온 단어만 sg=
print('3) word2vec 모델 학습 완료: ', time.time() - start)#현재시간-시작시간=걸린시간

print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료: ', time.time() - start)#현재시간-시작시간=걸린시간

print("corpus_count : ", model.corpus_count)
print("corpus_total_words : ", model.corpus_total_words)
