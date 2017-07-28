'''
Created on 2017-07-28 16:29

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 Pandas 시계열 자료 다루기

 pandas에서 일반적인 테이블 형태의 자료와 시계열 자료의 차이점은 인덱스(Index)에 있다.
 일반적인 테이블 형태의 자료는 임의의 값을 인덱스로 가질 수 있지만 시계열 자료는 다음 클래스를 인덱스로 가진다.

    DatetimeIndex : 타임스탬프
"""

"""
 DatatimeIndex

 DatetimeIndex는 특정한 순간에 기록된 타임스탬프(timestamp) 형식의 시계열 자료를 
 다루기 위한 인덱스이다. 타임스탬프 인덱스는 반드시 일정한 간격으로 
 자료가 있어야 한다는 조건은 없다.


 DatetimeIndex 타입의 인덱스는 보통 다음 방법으로 생성한다.
    pd.to_datetime 함수
    pd.date_range 함수
"""

# to_datetime
date_str = ["2017, 07, 01", "2017, 07, 04", "2017, 07, 05", "2017, 07, 06"]
idx = pd.to_datetime(date_str)
print(idx)
# DatetimeIndex(['2017-07-01', '2017-07-04', '2017-07-05', '2017-07-06'], dtype='datetime64[ns]', freq=None)

np.random.seed(0)
s = pd.Series(np.random.randn(4), index=idx)
print(s)
# 2017-07-01    1.764052
# 2017-07-04    0.400157
# 2017-07-05    0.978738
# 2017-07-06    2.240893
# dtype: float64

print(type(s.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>


div()
# date_range
# 시작일과 종료일 또는 시작일과 기간을 입력하면 범위 내의 날짜 및 시간 인덱스 생성
# freq 인수로 빈도 지정 가능

# start, end 지정
print(pd.date_range("2017-07-01", "2017-07-31"))

# start, periods 지정
print(pd.date_range(start="2017-08-01", periods=30))

# start, end, freq 지정 (freq=B : business day frequency) 주말은 휴업이라 표시 안함
print(pd.date_range("2016-4-1", "2016-4-30", freq="B"))

# freq=MS : 매월 1일. month start frequency
print(pd.date_range("2016-12-05", "2017-12-31", freq="MS"))

# freq=M : 매월 말일. month end frequency
print(pd.date_range("2017-01-01", "2017-12-31", freq="M"))

# freq=BMS : 매월 근무 시작 날짜(주말은 제외) business month start frequency
# freq=BM : 매월 근무 마지막 날짜 	business month end frequency
# freq=W-MON : 매주 월요일 날짜 	weekly frequency + Monday
# freq=WOM-2THU : 매월 두번째 목요일 날짜.
# freq=Q : 분기별 마지막 날짜


# shift 연산 : 날짜 이동
div()

ts = pd.Series(np.arange(10, 50, 10), index=pd.date_range("2017-01-01", periods=4, freq="M"))
print(ts)
# 2017-01-31    10
# 2017-02-28    20
# 2017-03-31    30
# 2017-04-30    40

# data값이 한칸 밀림
print(ts.shift(1))
# 2017-01-31     NaN
# 2017-02-28    10.0
# 2017-03-31    20.0
# 2017-04-30    30.0

# data값이 한칸씩 당겨짐
print(ts.shift(-1))
# 2017-01-31    20.0
# 2017-02-28    30.0
# 2017-03-31    40.0
# 2017-04-30     NaN

# 날짜 빈도 변경

# 날짜가 다음번째 날짜로 밀림
print(ts.shift(1, freq="M"))
# 2017-02-28    10
# 2017-03-31    20
# 2017-04-30    30
# 2017-05-31    40

# freq를 W로 변경 : M+W 매달 첫번째 일요일
print(ts.shift(1, freq="W"))

"""
 리샘플링 (Resampling)

 up-sampling : 구간이 작아지는 경우
 down-sampling: 구간이 커지는 경우
"""
div()
ts = pd.Series(np.arange(1, 101), index=pd.date_range("2000-1-1", periods=100, freq="D"))
print(ts.head(20))

# resample() 매주 월요일 날짜 설정
# 1주 평균 구하기
print(ts.resample('W').mean())

print(ts.resample('M').first())

# freq = T : 분단위
div()

ts = pd.Series(np.arange(1, 61), index=pd.date_range("2000-1-1", periods=60, freq="T"))
print(ts.head(20))

# 10분 단위로 더하기
print(ts.resample("10min").sum())

#
print(ts.resample("10min", closed="right").sum())

#
print(ts.resample("10min").ohlc())

#
print(ts.resample("10min", closed="right").ohlc())

#
print(ts.resample("30s").ffill())

#
print(ts.resample("30s").bfill())