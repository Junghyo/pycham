'''
Created on 2017-08-01 13:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
문서 전처리

모든 데이터 분석 모형은 숫자로 구성된 고정 차원 벡터를 독립 변수로 하고 있으므로 
문서(document)를 분석을 하는 경우에도 숫자로 구성된 특징 벡터(feature vector)를 
문서로부터 추출하는 과정이 필요하다. 
이러한 과정을 문서 전처리(document preprocessing)라고 한다.
"""


"""
BOW (Bag of Words)
문서를 숫자 벡터로 변환하는 가장 기본적인 방법은 BOW (Bag of Words) 이다. 
BOW 방법에서는 전체 문서 {D1,D2,…,Dn}를 구성하는 
고정된 단어장(vocabulary) {W1,W2,…,Wm}를 만들고  
Di라는 개별 문서에 단어장에 해당하는 단어들이 포함되어 있는지를 표시하는 방법이다.
먄약 단어 Wj가 문서Di에 있으면 Xij = 1
"""

"""
Scikit-Learn 의 문서 전처리 기능

Scikit-Learn 의 feature_extraction.text 서브 패키지는 다음과 같은 문서 전처리용 클래스를 제공한다.

CountVectorizer:
문서 집합으로부터 단어의 수를 세어 카운트 행렬을 만든다.
TfidfVectorizer:
문서 집합으로부터 단어의 수를 세고 TF-IDF 방식으로 단어의 가중치를 조정한 카운트 행렬을 만든다.
HashingVectorizer:
hashing trick 을 사용하여 빠르게 카운트 행렬을 만든다.
"""

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
    'The last document?',
]
vect = CountVectorizer()
vect.fit(corpus)
vect.vocabulary_
print(vect.vocabulary_)
print(vect.transform(corpus).toarray())

import urllib.request as ur
import json
import string
import konlpy
from konlpy.utils import pprint
from konlpy.tag import Hannanum
import matplotlib as mpl
import matplotlib.pylab as plt
hannanum = Hannanum()

url = "https://www.datascienceschool.net/download-notebook/708e711429a646818b9dcbb581e0c10a/"
request = ur.Request(url)
data = ur.urlopen(request)
json = json.loads(data.read())
cell = ["\n".join(c["source"]) for c in json["cells"] if c["cell_type"] == u"markdown"]

# 명사로 list화
docs = [w for w in hannanum.nouns(" ".join(cell)) if ((not w[0].isnumeric()) and (w[0] not in string.punctuation))]

# CountVectorizer: 문서 집합으로부터 단어의 수를 세어 카운트 행렬을 만든다.
div()
vect = CountVectorizer().fit(docs)
print(vect.vocabulary_)

# array화
print(vect.transform(docs).toarray())

# stop words : 필요없는 영어단어 삭제
from nltk.corpus import stopwords
vect = CountVectorizer(stop_words="english").fit(docs)
print(vect.vocabulary_)

# 토큰(token)
div()
# 한글자씩 자르기
vect = CountVectorizer(analyzer="char").fit(docs)
print(vect.vocabulary_)

import nltk
vect = CountVectorizer(tokenizer=nltk.word_tokenize).fit(docs)
print(vect.vocabulary_)


# n-그램
# n-그램은 단어장 생성에 사용할 토큰의 크기를 결정한다.
# 1-그램은 토큰 하나만 단어로 사용하며
# 2-그램은 두 개의 연결된 토큰을 하나의 단어로 사용한다.
div()
vect = CountVectorizer(ngram_range=(2,2)).fit(docs)
print(vect.vocabulary_)

"""
빈도수

max_df, min_df 인수를 사용하여 문서에서 토큰이 나타난 횟수를 기준으로 단어장을 구성할 수도 있다. 
토큰의 빈도가 max_df로 지정한 값을 초과 하거나 min_df로 지정한 값보다 작은 경우에는 무시한다. 
인수 값은 정수인 경우 횟수, 부동소수점인 경우 비중을 뜻한다.
"""
vect = CountVectorizer(max_df=4, min_df=2).fit(docs)
print(vect.vocabulary_)
print(vect.stop_words_)

"""
TF-IDF
TF-IDF(Term Frequency – Inverse Document Frequency) 인코딩은 
단어를 갯수 그대로 카운트하지 않고 모든 문서에 공통적으로 들어있는 단어의 경우 
문서 구별 능력이 떨어진다고 보아 가중치를 축소하는 방법이다.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
tfidv = TfidfVectorizer().fit(cell)
