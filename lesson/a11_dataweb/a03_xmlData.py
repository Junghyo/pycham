'''
Created on 2017-07-31 12:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd


"""
 1. file로 xml data 읽기
    1). 필요한 package import
        import xml.etree.ElementTree as ET
    2) 계층형 객체로 변경
        doc = ET.parse(파일이름)
    3) root를 지정
        계층형 객체.getroot()

 2. url xml data읽기
    1) url을 통해 요청객체 가져오기
        url = "www.~~~~"
    2) request를 통해 응답객체(결과처리) 가져오기
        request = urllib.rq.Request(url)
        response = urllib.rq.urlopen(request)
    3) 계층형으로 변경
        tree = ET.parse(response)
    4) root 접근하기
        rt = tree.getroot()
"""

# package import
import requests as rq
import xml.etree.ElementTree as ET
import urllib.request as ur

# 외부주소 : url
url = "https://apis.daum.net/local/v1/search/category.xml?apikey=465b06fae32febacbc59502598dd7685&code=AT4&location=37.514322572335935,127.06283102249932&radius=20000"

# response 가져오기(url -> request -> response)
request = ur.Request(url)
response = ur.urlopen(request)

# 계층형으로 변경
tree = ET.parse(response)

# root 접근
root = tree.getroot()
print(root)

# 실제 데이터를 찾기
item = root.findall("item")
print(item)

# 전체 데이터를 담기 위한 list 객체 선언
a = []

# 하나 데이터를 list의 속성값을 지정해서 할당
# list["속성"] = find("xml명")

for i in item:
    # 단위객체 생성
    item = {}
    item["title"] = i.find("title").text
    # 단위객체의 데이터를 다 할당한 후, 배열에 append()로 할당
    item["latitude"] = i.find("latitude").text
    item["longitude"] = i.find("longitude").text
    a.append(item)

# 데이터 프레임 할당
df = pd.DataFrame(a, columns=["title", "latitude", "longitude"])
print(df)

# 외부주소 : url
url = "https://apis.daum.net/local/v1/search/category.xml?apikey=465b06fae32febacbc59502598dd7685&code=AT4&location=37.514322572335935,127.06283102249932&radius=20000"

# response 가져오기(url -> request -> response)
request = ur.Request(url)
response = ur.urlopen(request)
tree = ET.parse(response)
root = tree.getroot()

item = root.findall("item")
div()
for item in root.findall("item"):
    print(item.find("title").text)
