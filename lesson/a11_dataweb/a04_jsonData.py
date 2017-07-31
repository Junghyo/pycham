'''
Created on 2017-07-31 14:36

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 json
 
 1. 속성 - 값 쌍으로 이루어진 데이터 오브젝트 전달을 위한 개방형 표준 format
    ex) {"name" : "홍길동", "age" : 25}

 2. 인터넷에서 자료를 주고 받을 때, 표현방법 중 하나
 
 3. javascript 구문 형식의 언어 독립형 데이터 포맷
 
 4. 언어나 플랫폼(OS) 독립적으로 쉽게 이용
 
 5. python에선 json.loads("json형식의 문자열의 file or url")
 
 6. 표현방법
    list: [], dict:{key1 : value1, key2 : value2}, list+dict:[{key1 : value1, key2 : value2}]
"""

# package import
import json
import requests as rq

# url로 get방식 호출
url = "https://apis.daum.net/local/v1/search/category.json?apikey=465b06fae32febacbc59502598dd7685&code=AT4&location=37.514322572335935,127.06283102249932&radius=20000"
data = rq.get(url)
print(data) # <Response [200]>
print(data.text)

# json으로 data file loading
result = json.loads(data.text)

# 결과에 대한 최상위값
root = result["channel"]

# 핵심 데이터 key값 가져오기
item = root["item"]
print(item)

# DataFrame 처리
df = pd.DataFrame(item, columns=["address", "category", "title"])

print(df)

div()
root = result1["channel"]["item"]
print(root)

df = pd.DataFrame(root, columns=["address", "category", "title"])
print(df)