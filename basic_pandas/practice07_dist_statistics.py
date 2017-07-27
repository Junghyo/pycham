'''
Created on 2017-07-27 20:43

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
분포와 기술 통계
데이터의 수가 적으면 데이터의 값을 하나 하나 살펴볼 수 있지만 
데이터의 수가 많다면 숫자가 어떤 값 근처에 어떤 모양으로 모여 있는지 
전반적인 형태를 살펴보는 수밖에 없다. 
데이터 값의 전반적인 형태를 데이터의 분포(distribution)라고 한다.

일차원 데이터의 분포를 살펴보는 데는 다음과 같은 방법을 사용할 수 있다.

기술 통계 (descriptive statistics)
히스토그램 (histogram)
커널 밀도 (kernel density)

"""

"""
기술 통계
기술 통계(descriptive statistics)는 데이터 분포의 특징을 
대표할 수 있는 몇가지 숫자를 계산하여 이 숫자들로부터 데이터의 분포를 추측하는 방법이다. 
흔히 일반인들이 통계라고 부르는 것이 바로 기술 통계를 말한다.

데이터의 분포의 특징을 대표하는 값들로는

데이터의 숫자 (count)
평균 (mean, average)
분산 (variance)
표준 편차 (standard deviation)
최댓값 (maximum)
최솟값 (minimum)
중앙값 (median)
사분위수 (quartile)

등이 많이 사용된다. 이러한 기술 통계 수치들을 분포의 특성이라고도 한다.

사분위수(quartile)는 데이터를 크기대로 정렬하였을 때 1/4, 2/4, 3/4 위치에 있는 수를 말한다. 
각각 1사분위수, 2사분위수, 3사분위수라고 한다. 
1/4의 위치란 전체 데이터의 수가 만약 100개이면 25번째 순서, 즉 하위 25%를 말한다. 
따라서 2사분위수는 중앙값과 같다.

때로는 위치를 1/100 단위로 나눈 백분위수(percentile)을 사용하기도 한다. 
1사분위수는 25% 백분위수와 같다.
"""


x = np.array([ 18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
                2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13,
                1,   0,  16,  15,   2,   4,  -7, -18,  -2,   2,  13,  13,  -2,
               -2,  -9, -13, -16,  20,  -4,  -3, -11,   8, -15,  -1,  -7,   4,
               -4, -10,   0,   5,   1,   4,  -5,  -2,  -5,  -2,  -7, -16,   2,
               -3, -15,   5,  -8,   1,   8,   2,  12, -11,   5,  -5,  -7,  -4])

print(len(x)) # 78

print(np.mean(x))   # 0.692307692308

print(np.var(x))    # 96.0591715976

print(np.std(x))    # 9.80097809393
print(np.sqrt(np.var(x)))   # 9.80097809393
# 표준편차는 분산의 제곱근

print(np.max(x))     # 23

print(np.min(x))     # -24

print(np.median(x)) # 0.5 중앙값

print(np.percentile(x, 25)) # -5.75 : 1사분위수

print(np.percentile(x, 50)) # 0.5 : 2사분위수 = mean

print(np.percentile(x, 75)) # 5.0 : 3사분위수

print(np.percentile(x, 100)) # 23.0 : 4사분위수 = max

# pandas의 describe()를 이용하면 이러한 기술 통계값을 한번에 게산 가능


s = pd.Series(x)
print(s)

print(s.describe())
# count    78.000000
# mean      0.692308
# std       9.864416
# min     -24.000000
# 25%      -5.750000
# 50%       0.500000
# 75%       5.000000
# max      23.000000