from konlpy.tag import Okt

okt = Okt()
text = "아버지가 방에 들어갑니다."

morphs = okt.morphs(text)
print(morphs)

pos = okt.pos(text)
print(pos)

nouns = okt.nouns(text)
print(nouns)

text = "오늘 날씨가 좋아요ㅎㅎ~"
print(okt.normalize(text))
print(okt.phrases(text))