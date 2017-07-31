'''
Created on 2017-07-31 20:08

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
NLTK 자연어 처리 패키지 소개

NLTK(Natural Language Toolkit) 패키지는 교육용으로 
개발된 자연어 처리 및 문서 분석용 파이썬 패키지다. 
다양한 기능 및 예제를 가지고 있으며 실무 및 연구에서도 많이 사용된다.

NLTK 패키지가 제공하는 주요 기능은 다음과 같다.

샘플 corpus 및 사전
토큰 생성(tokenizing)
형태소 분석(stemming/lemmatizing)
품사 태깅(part-of-speech tagging)
구문 분석(syntax parsing)
"""

"""
샘플 corpus

corpus는 분석 작업을 위한 샘플 문서 집합을 말한다. 
단순히 소설, 신문 등의 문서를 모아놓은 것도 있지만 
대부분 품사. 형태소, 등의 보조적 의미를 추가하고 
쉬운 분석을 위해 구조적인 형태로 정리해 놓은 것이 많다.
"""
import nltk

# 이러한 corpus 자료는 설치시에 제공되는 것이 아니라 download 명령으로 사용자가 다운로드 받아야 한다.
# nltk.download('averaged_perceptron_tagger')
# nltk.download("gutenberg")
# nltk.download('punkt')
# nltk.download('reuters')
# nltk.download("stopwords")
# nltk.download("taggers")
# nltk.download("webtext")
# nltk.download("wordnet")

print(nltk.corpus.gutenberg.fileids())

# 예제 데이터 로딩
emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")


"""
토큰 생성(tokenizing)

문서를 분석하기 위해서는 우선 긴 문자열을 분석을 위한 작은 단위로 나누어야 한다. 
이 문자열 단위를 토큰(token)이라고 한다.
"""

from nltk.tokenize import word_tokenize
print(word_tokenize(emma_raw[50:100]))
# ['Emma', 'Woodhouse', ',', 'handsome', ',', 'clever', ',', 'and', 'rich', ',', 'with', 'a']

div()
from nltk.tokenize import RegexpTokenizer
t = RegexpTokenizer("[\w]+")
print(t.tokenize(emma_raw[50:100]))
# ['Emma', 'Woodhouse', 'handsome', 'clever', 'and', 'rich', 'with', 'a']

div()
from nltk.tokenize import sent_tokenize
print(sent_tokenize(emma_raw[50:100]))
# ['Emma Woodhouse, handsome, clever, and rich, with a']

"""
형태소 분석

형태소 분석이란 어근, 접두사/접미사, 품사(POS, part-of-speech) 등 
다양한 언어적 속성의 구조를 파악하는 작업이다. 

구체적으로는 다음과 같은 작업으로 나뉜다.

stemming (어근 추출)
lemmatizing (원형 복원)
POS tagging (품사 태깅)
"""

# Stemming and lemmatizing
div()
from nltk.stem import PorterStemmer
st = PorterStemmer()
print(st.stem("eating"))
# eat

from nltk.stem import LancasterStemmer
st = LancasterStemmer()
print(st.stem("shopping"))
# shop

from nltk.stem import RegexpStemmer
st = RegexpStemmer("ing")
print(st.stem("going"))
# go


from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
print(lm.lemmatize("cooking"))
print(lm.lemmatize("cooking", pos="v"))
print(lm.lemmatize("cookbooks"))
# cooking
# cook
# cookbook

print(WordNetLemmatizer().lemmatize("believes"))
print(LancasterStemmer().stem("believes"))
# belief
# believ

# POS tagging : POS(part-of-speech)는 품사를 말한다.
div()
from nltk.tag import pos_tag
tagged_list = pos_tag(word_tokenize(emma_raw[:100]))
print(tagged_list)

div()
from nltk.tag import untag
print(untag(tagged_list))