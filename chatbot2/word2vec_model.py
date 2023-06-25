from gensim.models import Word2Vec

model = Word2Vec.load('nvmc.model')
print("corpus_total_words : ", model.corpus_total_words)

print('사랑 : ', model.wv['사랑'])#nvmc.model에서 사랑이라는 단어의 임베딩 벡터

print("일요일 = 월요일\t", model.wv.similarity(w1='일요일', w2='월요일')) #유사도(단어형태자체가비슷)
print("안성기 = 배우\t", model.wv.similarity(w1='안성기', w2='배우'))#유사도(단어형태는다르지만의미가비슷)
print("대기업 = 삼성\t", model.wv.similarity(w1='대기업', w2='삼성'))#유사도(단어형태는다르지만의미가비슷)
print("일요일 = 삼성\t", model.wv.similarity(w1='일요일', w2='삼성'))#유사도 낮음
print("히어로 = 삼성\t", model.wv.similarity(w1='히어로', w2='삼성'))#유사도 낮음

print(model.wv.most_similar("안성기", topn=5))#안성기와 가장 비슷한 단어5개 top5
print(model.wv.most_similar("시리즈", topn=5))#시리즈와 가장 비슷한 단어5개 top5