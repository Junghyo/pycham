'''
Created on 2017-08-02 21:03

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
1. 누락된 데이터를 삽입/삭제
    - resample()
2. date_range
    1) 범위를 지정해서 
        start : 시작일
        end : 종료일
        시작일, 범위(periods)를 입력해서 범위 
        날짜 및 시간 인덱스 생성..
    2) freq 빈도 지정.
        B : business day
        MS : 월의 시작 month start
        M :월의 마지막 날짜.
        M,T,S : 매시간, 분, 초
        BM, BMS : 일을 하는 월의 마지막과 시작 날짜.
        W-MON : 요일
        WOM-1MON : 월의 첫번째 월요일..
"""
from datetime import datetime

# 날짜 start와 end 지정
print(pd.date_range("2017-01-01", "2017-12-31"))
# DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
#                '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-08',
#                '2017-01-09', '2017-01-10',
#                ...
#                '2017-12-22', '2017-12-23', '2017-12-24', '2017-12-25',
#                '2017-12-26', '2017-12-27', '2017-12-28', '2017-12-29',
#                '2017-12-30', '2017-12-31'],
#               dtype='datetime64[ns]', length=365, freq='D')

# start와 periods 지정 8월 1일부터 일단위로 100개 뽑기
print(pd.date_range(start='2017-8-1', periods=100))

# 현재날짜 부터 월말 단위로 100개 뽑기
print(pd.date_range(start=datetime.now(), freq="M", periods=100))