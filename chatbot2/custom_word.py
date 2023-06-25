from konlpy.tag import Komoran

#userdic=고유명사 추가
komoran = Komoran(userdic='./user_dic.tsv')#user_dic.tsv파일=([단어]Tab[품사])형식으로 저장
text = "자연어처리는 엔엘피라고 하지." #엔엘피=명시되지 않는 명사
text2 = "나 저번주에 스즈메의 문단속을 봤어."#스즈메의 문단속=명시되지 않는 명사(하지만 공백이 있어서 지정X)
pos = komoran.pos(text)
pos2 = komoran.pos(text2)
print(pos)
print(pos2)