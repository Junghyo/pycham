'''
Created on 2017-07-31 11:40

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import requests as rq
"""
 web에서 데이터 로딩 방식(get)
 
 1. params01 = {"param1": "value1", "param2": "value2"}
 2. res = request.get(URL, params=params01)
 http://localhost:8080/web?param1=value1&param2=value2
"""
url = "http://www.naver.com"
data = rq.get(url)
print(data)
print(data.text)

# 내부 서버에서 데이터 가져오기
url = "http://localhost:14261/session/viewhtmledc1d8e4ee9/index.html"
data = rq.get(url)
print(data)
print(data.text)