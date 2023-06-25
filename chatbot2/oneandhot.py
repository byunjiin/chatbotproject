from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "산하고 나무하고 누가 누가 더 푸를까?"

nouns = komoran.nouns(text)
print(nouns)

dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)