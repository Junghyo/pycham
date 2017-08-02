'''
Created on 2017-08-02 20:52

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
# pandas 시계열 자료
    테이블 형태 자료는 index 포함
    시계열 자료 DatetimeIndex(타임스탬프) 포함

# DatetimeIndex
    1. 특정 순간에 기록된 시계열자료를 위한 인덱스 : 타임스탬프
    2. 일정한 간격은 자료를 조건으로 하지 않는다.
    3. 인덱스 생성..
        pd.to_datetime() 함수..
        pd.date_range()
"""
date = ["2017/8/9", "2017/8/16", "2017/8/23", "2017/8/30", "2017/9/6"]
print(date) # ['2017/8/9', '2017/8/16', '2017/8/23', '2017/8/30', '2017/9/6']
print(type(date))   # <class 'list'>

idx = pd.to_datetime(date)

print(idx)
# DatetimeIndex(['2017-08-09', '2017-08-16', '2017-08-23', '2017-08-30',
#                '2017-09-06'],
#               dtype='datetime64[ns]', freq=None)

print(type(idx))    # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

np.random.seed(0)
s = pd.Series(np.random.rand(5), index=idx)
print(s)