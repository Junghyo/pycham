'''
Created on 2017-07-31 20:44

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
# import numpy as np
# import pandas as pd


"""
 konlpy
 
 konlpy는 한국어 정보처리를 위한 파이썬 패키지이다.
 http://konlpy.org/ko/latest/
 https://github.com/konlpy/konlpy
 
 konlpy는 다음과 같은 다양한 형태소 분석, 태깅 라이브러리를 파이썬에서 쉽게 사용할 수 있도록 모아놓았다.

 Kkma
 http://kkma.snu.ac.kr/
 
 Hannanum
 http://semanticweb.kaist.ac.kr/hannanum/
 
 Twitter
 https://github.com/twitter/twitter-korean-text/
 
 Komoran
 http://www.shineware.co.kr/?page_id=835
 
 Mecab
 https://bitbucket.org/eunjeon/mecab-ko-dic
 
 konlpy 는 다음과 같은 기능을 제공한다.
 한국어 corpus
 한국어 처리 유틸리티
 형태소 분석 및 품사 태깅
"""

# 한국어 corpus

from konlpy.corpus import kolaw
print(kolaw.fileids())
c = kolaw.open('constitution.txt').read()
print(c[:100])

from konlpy.corpus import kobill
print(kobill.fileids())

d = kobill.open("1809890.txt").read()
print(d[:100])


"""
한국어 처리 유틸리티

konlpy에는 유니코드 한글 문자열이 리스트나 딕셔너리의 내부에 있을 때도 
한글 글자 모양을 정상적으로 보여주는 pprint 유틸리티 함수를 제공한다.
"""
div()

x = [u"한글", {u"한글 키": [u"한글 밸류1", u"한글 밸류2"]}]
print(x)
# [u'\ud55c\uae00', {u'\ud55c\uae00 \ud0a4': [u'\ud55c\uae00 \ubc38\ub9581', u'\ud55c\uae00 \ubc38\ub9582']}]
# 이렇게 나온다는데 정상적으로 나옴.

from konlpy.utils import pprint
pprint(x)

# ['한글', {'한글 키': ['한글 밸류1', '한글 밸류2']}]


"""
 형태소 분석
 
konlpy는 tag 서브패키지에서 형태소 분석을 위한 5개의 클래스를 제공한다.
Kkma
Hannanum
Twitter
Komoran
Mecab

이 클래스는 다음과 같은 메서드를 대부분 제공한다.

morphs : 형태소 추출
nouns : 명사 추출
pos : pos 태깅
"""
from konlpy.tag import *

hannanum = Hannanum()
kkma = Kkma()
twitter = Twitter()

# 명사 추출
# 문자열에서 명사만 추출하려면 noun 명령을 사용

pprint(hannanum.nouns(c[:65]))

div()

pprint(kkma.nouns(c[:65]))

div()

pprint(twitter.nouns(c[:65]))

# 형태소 추출
# 명사 뿐 아니라 모든 품사의 형태소를 알아내려면 morphs라는 명령을 사용한다.
div()

pprint(hannanum.morphs(c[:65]))

div()

pprint(kkma.morphs(c[:65]))

div()

pprint(twitter.morphs(c[:65]))

"""
품사 태깅

pos 명령을 사용하면 품사(POS)가 붙어있는(tagging) 형태로 형태소 분석을 한다. 
다만 이 때 출력되는 품사의 정의 및 기호는 형태소 분석기 마다 다르므로 
각 형태소 분석기에 대한 문서를 찾아봐야 한다.

다음은 많이 쓰이는 형태소 분석기의 품사 기호를 비교한 자료이다.

https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0
"""
div()

pprint(hannanum.pos(c[:65], ntags=22))