'''
Created on 2017-08-07 15:01

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

문제1
어떤 동전을 15번 던졌더니 12번이 앞면이 나왔다. 이 동전은 휘어지지 않은 공정한 동전(fair coin)인가?
 H0 : 공정한 동전이다.
 H1 : not HO
"""
pvalue = sp.stats.binom(15, 0.5).cdf(12-1)
print(1 - pvalue)   # 0.017578125
# 유의수준 5%(0.05)하에서 검정시 p값이 0.0175로 유의수준보다 작기 때문에 H0기각.
# => 공정한 동전이 아니다.
# 유의수준이 1%라면 H0를 기각하지 못하고 채택하게 된다.


"""
문제2
어떤 트레이더의 일주일 수익률은 다음과 같다.:
-2.5%, -5%, 4.3%, -3.7% -5.6% 
이 트레이더는 돈을 벌어다 줄 사람인가, 아니면 돈을 잃을 사람인가?

H0 : 돈을 벌어다 줄 사람이다.
H1 : not H0
"""

x = np.array([-0.025, -0.05, 0.043, -0.037, -0.056])
t = x.mean()/(x.std(ddof=1)/np.sqrt(len(x)))
print(t)    # -1.40259214141
print(t, sp.stats.t(df=4).cdf(t))
# -1.40259214141 0.116692165096
# 유의수준 5%, 10%라면 pvalue가 0.11로 더 크기 때문에 귀무가설을 기각할 수 없다.
# 즉 돈을 잃을 사람이라고 할 수 있는 증거가 부족하다.