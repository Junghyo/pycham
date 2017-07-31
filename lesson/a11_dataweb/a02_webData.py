'''
Created on 2017-07-31 11:58

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import requests as rq
from lxml.html import parse # tag형식을 tree형식으로 변환시켜주는 모듈
import io

"""
 HTML data 가져오기
 
 1. tag 형식을 tree형식으로 전환
    lxml.html.parse( io.StringIO )
 
 2. 핵심되는 데이터의 root 객체 가져오기 : tree객체.getRoot()
 
 3. tag에 해당하는 data를 element의 list로 가져오기
    root객체.findall(".//tag명")
    ex) tables[0].findall(".//th") 타이틀
        tables[0].findall(".//td") data 내용
        
 4. 데이터 찾기
    root객체.find("form") : root객체 tag 하위에 from과 일치하는 첫번째 데이터 return, 없으면 None
    특정한 데이터의 첫번재 데이터를 찾고싶다면?
    root객체.findtext("from")
    
 5. 속성찾기
    elements의 get("속성") : 속성값 가져오기
"""
# 사용할 주소
url = "http://finance.daum.net/quote/kospi_yyyymmdd.daum"

# 응답 받을 response 개체 만들기
data = rq.get(url)

# tag를 계층형으로 변경
doc = parse(io.StringIO(data.text))

# 최상의 root() 받기
root = doc.getroot()

# 핵심 데이터가 table 안에 있으므로 table tag로 접근
tables = root.findall(".//table")

# column으로 쓸 데이터
title = tables[0].findall(".//th")

cols = []
for t in title:
    print(t.text_content())
    cols.append(t.text_content())

# 실제 데이터내용을 담을 부분
content = tables[0].findall(".//td")
values = []

for ct in content:
    if ct.text_content() != "":
        print(ct.text_content())
        values.append(ct.text_content())

# 나열된 data를 9개 단위로 변경
a = np.array(values).reshape(10, -1)
print(a)

# DataFrame 만들기
df = pd.DataFrame(a, columns=cols)
print(df)