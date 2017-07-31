'''
Created on 2017-07-31 15:17

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

# 대상이 되는 2개의1 차원 배열
s1 = pd.Series([84900, 81800, 1767], index=["daum", "naver", "nexen"])
s2 = pd.Series([86100, 87100, 1776, 295000], index=["daum", "naver", "nexen", "NC"])
print(s1)
print(s2)

div()

# concat() : default
print(pd.concat([s1, s2]))
# daum      84900
# naver     81800
# nexen      1767
# daum      86100
# naver     87100
# nexen      1776
# NC       295000
# dtype: int64

print(np.concatenate((s1, s2)))
# [ 84900  81800   1767  86100  87100   1776 295000]

# concat() : axis=1
div()
print(pd.concat([s1, s2], axis=1))
#              0       1
# NC         NaN  295000
# daum   84900.0   86100
# naver  81800.0   87100
# nexen   1767.0    1776

# join_axes : join에 참여할 index를 설정
# keys를 이용하여 컬럼명을 붙이는 기능
div()
print(pd.concat([s1, s2], axis=1, join_axes=[["daum", "naver", "nexen", "NC"]],
        keys=["2017-07-31", "2017-08-01"]))

#        2017-07-31  2017-08-01
# daum      84900.0       86100
# naver     81800.0       87100
# nexen      1767.0        1776
# NC            NaN      295000
