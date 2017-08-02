'''
Created on 2017-08-02 20:56

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
from datetime import datetime

"""
날짜데이터..
1. 기본적인 시계열 종류
    1) 파이썬 문자열.
    2) Series : datetime객체/타임스탬프를 index
    3) indexing은 Series와 동일
    4) 날짜 --> 문자열, 연도나 월까지만도가능
    5) slicing은 Series와 동일
    6) truncate() : before, after
    7) 날짜가 중복된 경우, 기술 통계 수행.. groupby대입.
"""

dates =[datetime(2017,8,2),datetime(2017,8,9),datetime(2017,8,16),
        datetime(2017,8,23),datetime(2017,8,30),datetime(2017,9,6)]
print(dates)
# [datetime.datetime(2017, 8, 2, 0, 0), datetime.datetime(2017, 8, 9, 0, 0),
# datetime.datetime(2017, 8, 16, 0, 0), datetime.datetime(2017, 8, 23, 0, 0),
# datetime.datetime(2017, 8, 30, 0, 0), datetime.datetime(2017, 9, 6, 0, 0)]
print(type(dates))

np.random.seed(0)
ts = pd.Series(np.random.rand(6), index=dates)
print(ts)
# 2017-08-02    0.548814
# 2017-08-09    0.715189
# 2017-08-16    0.602763
# 2017-08-23    0.544883
# 2017-08-30    0.423655
# 2017-09-06    0.645894
print(type(ts.index)) # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# 3번쨰 데이터 출력
div()

print(ts[2])
print("3번째 데이터 출력",ts[ts.index[2]])

# 문자열로 출력
print("문자열로 index(08/07)된 내용 출력1", ts['2017/8/9'])
print("문자열로 index(08/07)된 내용 출력2", ts['20170809'])
print("월단위문자열로 index된 내용 출력", ts['2017-8'])
print("년도로 출력", ts['2017'])

# slicing
div()
print("slicing 처리,",ts['2017-08-16':'2017-08-30'])

## truncate : before after
##  해당 데이터는 잘라서 보여줌..
print("truncate 처리1:\n",ts.truncate(before='2017-08-16'))
print("truncate 처리2\n",ts.truncate(after='2017-08-16'))