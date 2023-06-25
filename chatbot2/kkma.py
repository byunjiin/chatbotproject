from konlpy.tag import Kkma

kkma = Kkma()
text = "아버지가 방에 들어갑니다"

morphs = kkma.morphs(text)
print(morphs) #morphs=형태소만 추출

pos = kkma.pos(text)
print(pos) #pos=형태소를 추출하고 명사,조사 같은태그도 

nouns = kkma.nouns(text)
print(nouns)#nouns=명사만 추출

sentences = "오늘 날씨는 어때요? 내일은 덥다던데"
s = kkma.sentences(sentences)
print(s)