'''
Created on 2017-08-03 19:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import scipy as sp
import scipy.stats as stats

"""
 대표값
 
 평균, 기댓값, 중앙값
 
 중앙값
 n이 홀수 : (n+1)/2
 n이 짝수 : n/2의 값과 n/2 + 1 값의 평균
"""

"""
Python에서는 다음과 같은 numpy 함수를 사용하여 계산할 수 있다.

mean()
nanmean()
median()
argmax()
histogram()
"""
np.random.seed(0)
x = np.random.normal(size=1000)

# 평균
print(np.mean(x))

# 중앙값
print(np.median(x))

n, bins = np.histogram(x, bins=np.linspace(-10, 10, 20))
print(n)
print(bins)
plt.plot(bins[1:]+bins[:-1], n)
plt.show()

# argmax : 최대값의 index
M = np.argmax(n)
print(M)
print(bins[M], bins[M+1])


"""
Python에서 샘플 분산과 샘플 표준 편차는 numpy의 다음 함수들을 사용한다.

var()
std()
nanvar()
nanstd()

"""

sp.random.seed(0)
# 평균1, 분산 4의 정규분포를 따르는 랜덤데이터 1000개 추출
# mean=0, standard deviation=2
x = sp.stats.norm(0, 2).rvs(1000)
print("x's var", sp.var(x))
# unbiased estimator : 불편추정량
print("x's unbiased estimator", sp.var(x, ddof=1))
print("x's sd", sp.std(x))
print("x's mean", sp.mean(x))