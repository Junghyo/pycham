'''
Created on 2017-07-28 15:11

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

# chuncksize : 로딩할 때 한번에 읽어 올 데이터 건수.
p = pd.read_csv("good.csv", header=None, chunksize=2)
print(p)

# 반복문을 통해서 데이터 가져오기
for i in p:
    print(i.sort_values(by=2, ascending=False))
    print("="* 50)

# sep= : 구분자
a = pd.read_csv("fruit.csv", header=None, sep="|")
print(a)

# csv 객체를 통한 reader를 활용하여 파일 읽기. delimiter 지원
div()
import csv
lines = list( csv.reader(open("fruit.csv"),delimiter="|") )
print(lines)

# list -> DataFrame
frame = pd.DataFrame(lines, columns=["name", "count", "price"])
print(frame)

"""
 csv 파일 저장
 
 1. Series, DataFrame : to_csv()로 파일 경로지정.
 2. sep : 구분자
 3. na_rep : NaN값을 원하는 형식으로
 4. index, header값을 False로 하면 없앨 수 있음
"""
