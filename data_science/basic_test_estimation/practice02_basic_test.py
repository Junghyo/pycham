'''
Created on 2017-08-07 15:12

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
 scipy를 사용한 기초적인 검정
 
이항 검정 (Binomial test)
카이 제곱 검정 (Chi-square test)
단일 표본 z-검정 (One-sample z-test)
단일 표본 t-검정 (One-sample t-test)
독립 표본 t-검정 (Independent-two-sample t-test)
대응 표본 t-검정 (Paired-two-sample t-test)
분산 검정 (Chi squared variance test)
등분산 검정 (Equal-variance test)
정규성 검정 (Normality test)
"""

"""
이항 검정 (Binomial test)

이항 검정은 이항 분포를 이용하여 Bernoulli 분포 모수  θθ 에 대한 가설을 조사하는 검정 방법이다.
scipy stats 서브패키지의 binom_test 명령을 사용한다. 디폴트 귀무 가설은 θ=0.5 이다.
"""

# 데이터 갯수  N=10 , 확률이 0.5인 경우 이항 검정
N = 10
p = 0.5
np.random.seed(0)
x = sp.stats.bernoulli(p).rvs(N)
n = np.count_nonzero(x)
print(n)    # 7
print(sp.stats.binom_test(n, N, p=0.5))    # 0.34375
# p값이 0.34로 유의수준 0.05보다 높아 기각할 수 없다. 따라서 p = 0.5이다.

# 데이터 갯수  N=100 , 확률이 0.5인 경우 이항 검정
N = 100
p = 0.5
np.random.seed(0)
x = sp.stats.bernoulli(p).rvs(N)
n = np.count_nonzero(x)
print(n)    # 49
print(sp.stats.binom_test(n, N))
# 0.920410762613
# p값이 0.92로 매우 높아 귀무가설을 기각할 수 없다. 따라서 p = 0.5

# 데이터 갯수  N=100, 실제 모수  θ=0.35 인 경우
N = 100
p = 0.35
np.random.seed(0)
x = sp.stats.bernoulli(p).rvs(N)
n = np.count_nonzero(x)
print(n)    # 31
print(sp.stats.binom_test(n, N, p=0.5))
# 0.000183143224882
# p값이 작아 귀무가설을 기각한다. 따라서 확률은 0.5가 아니다.

"""
카이 제곱 검정 (Chi-square test)


카이 제곱 검정은 goodness of fit 검정이라고도 부른다. 
카테고리 분포의 모수  θ=(θ1,…,θK)에 대한 가설을 조사하는 검정 방법이다. 
scipy stats 서브패키지의 chisquare 명령을 사용한다. 디폴트 귀무 가설은  θ=(1/K, …, 1/K)이다.
"""
div()

# 데이터 갯수  N=10, 실제 모수  θ=(0.25, 0.25, 0.25, 0.25)인 경우
N = 10
K = 4
p = np.ones(K)/K
print(p)    # [ 0.25  0.25  0.25  0.25]
np.random.seed(0)

# 0~3까지 10개 추출.
x = np.random.choice(K, N, p=p)
print(x)    # [2 2 2 2 1 2 1 3 3 1]
n = np.bincount(x, minlength=K)
print(n)    # [0 3 5 2]

print(sp.stats.chisquare(n))
# Power_divergenceResult(statistic=5.1999999999999993, pvalue=0.157724450396663)
# 유의확률이 0.16으로 귀무가설을 기각할 수 없다. 따라서 p = [ 0.25  0.25  0.25  0.25]

# 데이터 갯수  N=100, 실제 모수  θ=(0.35,0.30,0.20,0.15)인 경우
N = 100
K = 4
p = np.array([0.35, 0.30, 0.20, 0.15])
np.random.seed(0)
x = np.random.choice(K, N, p=p)
n = np.bincount(x, minlength=K)
print(n)    # [37 32 20 11]
print(sp.stats.chisquare(n))
# Power_divergenceResult(statistic=16.559999999999999, pvalue=0.00087034719789121269)
# p값이 0.0008로 귀무가설을 기각한다. 따라서 p는 [ 0.25  0.25  0.25  0.25]가 아니다.


"""
단일 표본 z-검정 (One-sample z-test)

단일 표본 z-검정은 분산 σ2의 값을 정확히 알고 있는 
정규 분포의 표본에 대해 기댓값을 조사하는 검정방법이다. 
단일 표본 z-검정의 경우에는 scipy에 별도의 함수가 준비되어 있지 않으므로 
norm 명령의 cdf 메서드를 사용하여 직접 구현해야 한다.
"""
# 데이터 갯수  N=10 , 실제 모수  μ=0인 경우
div()

N = 10
mu = 0
np.random.seed(0)
x = sp.stats.norm(loc=0, scale=1).rvs(N)
print(x)

def ztest(x):
    z = (x.mean() - mu)/np.sqrt(1/len(x))
    return z, 2 * sp.stats.norm().sf(np.abs(z))
print(ztest(x))
# (2.3338341854824276, 0.019604406021683538)
# 0.19로 귀무가설을 기각하여 μ=0 아니라고 할 수 있으나 이 검정 결과는 잘못된 것이다.
# 데이터가 10개로 부족하기 때문
# 귀무가설이 진실인데도 기각하는 오류를 제 1종 오류라고 한다.

# 데이터 갯수  N=100 , 실제 모수  μ=0 인 경우
N = 100
mu = 0
np.random.seed(0)
x = sp.stats.norm(loc=0, scale=1).rvs(N)

def ztest(x):
    z = (x.mean()-mu) / (1 / np.sqrt(N))
    return z, 2 * sp.stats.norm().sf(np.abs(z))

print(ztest(x))
# (0.59808015534484993, 0.54978645086241684)
# p값이 0.549로 기각 할 수 없다. 따라서 μ=0이다.


"""
단일 표본 t-검정 (One-sample t-test)

단일 표본 t-검정은 정규 분포의 표본에 대해 기댓값을 조사하는 검정방법이다.
scipy의 stats 서브 패키지의 ttest_1samp 명령을 사용한다. 
ttest_1samp 명령의 경우에는 디폴트 모수가 없으므로 popmean 인수를 사용하여 직접 지정해야 한다.
"""
# 데이터 갯수  N=10 , 실제 모수  μ=0
div()
N = 10
mu = 0
np.random.seed(0)
x = sp.stats.norm(loc=mu, scale=1).rvs(N)
sns.distplot(x, kde=False, fit=sp.stats.norm)
# plt.show()
print(sp.stats.ttest_1samp(x, popmean=mu))
# Ttest_1sampResult(statistic=2.2894396723896699, pvalue=0.047818464908570578)
# p값이 0.047로 귀무가설을 기각하지만 표본 수가 불충분하여 오류가 발생했을 확률이 높다.

# 데이터 갯수  N=100 , 실제 모수  μ=0
N = 100
mu = 0
np.random.seed(0)
x = sp.stats.norm(loc=mu, scale=1).rvs(N)
print(sp.stats.ttest_1samp(x, popmean=mu))
# Ttest_1sampResult(statistic=0.59042834028516977, pvalue=0.55624891586946745)
# p값이 0.55로 귀무가설을 기각하지 못한다. 따라서 μ=0

"""

독립 표본 t-검정 (Independent-two-sample t-test)

독립 표본 t-검정(Independent-two-sample t-test)은 
간단하게 two sample t-검정이라고도 한다. 
두 개의 독립적인 정규 분포에서 나온 두 개의 데이터 셋을 사용하여 
두 정규 분포의 기댓값이 동일한지를 검사한다. 

scipy stats 서브패키지의 ttest_ind 명령을 사용한다. 
독립 표본 t-검정은 두 정규 분포의 분산값이 같은 경우와 
같지 않은 경우에 사용하는 검정 통계량이 다르기 때문에 
equal_var 인수를 사용하여 이를 지정해 주어야 한다.
"""
# 두 정규 분포의 기댓값이  μ1=0 ,  μ2=1 으로 다르고
# 분산은  σ1=σ2=1  으로 같으며 샘플의 수가  N1=N2=10 인 경우를 실행해 보자
# 등분산 조건
div()

N1 = N2 = 10
mu1 = 0
mu2 = 1
std1 = std2 = 1
np.random.seed(0)
x1 = sp.stats.norm(loc=mu1, scale=std1).rvs(N1)
x2 = sp.stats.norm(loc=mu2, scale=std2).rvs(N2)
# sns.distplot(x1, kde=False, fit=sp.stats.norm)
# sns.distplot(x2, kde=False, fit=sp.stats.norm)
# plt.show()

# equal_var = True : 등분산일 경우
print(sp.stats.ttest_ind(x1, x2, equal_var=True))
# Ttest_indResult(statistic=-1.6868710732328158, pvalue=0.10888146383913824)
# p값이 0.10으로 귀무가설 기각할 수 없다. 따라서   μ1=μ2
# 하지만 데이터 수가 적어 오류 발생 가능성이 높다.
# 귀무가설이 거짓인데도 이를 채택하는 경우를 제 2종 오류라고 한다.

# 데이터 수를 50, 100으로 각각 증가
N1 = 50
N2 = 100
mu1 = 0
mu2 = 1
std1 = std2 = 1
np.random.seed(0)
x1 = sp.stats.norm(loc=mu1, scale=std1).rvs(N1)
x2 = sp.stats.norm(loc=mu2, scale=std2).rvs(N2)
sns.distplot(x1, kde=False, fit=sp.stats.norm)
sns.distplot(x2, kde=False, fit=sp.stats.norm)
# plt.show()

print(sp.stats.ttest_ind(x1, x2, equal_var=True))
# Ttest_indResult(statistic=-5.4933508164927112, pvalue=1.6781161316695056e-07)
# 0.00000016781
# p값이 작아 귀무가설 기각. μ1과 μ2는 다르다.



"""
대응 표본 t-검정 (Paired-two-sample t-test)

대응 표본 t-검정은 독립 표본 t-검정을 두 집단의 샘플이 1대1 대응하는 경우에 대해 수정한 것이다. 
즉, 독립 표본 t-검정과 마찬가지로 두 정규 분포의 기댓값이 같은지 확인하기 위한 검정이다.

예를 들어 어떤 반의 학생들이 특강을 수강하기 전과 수강한 이후에 
각각 시험을 본 시험 점수의 경우에는 같은 학생의 두 점수는 대응할 수 있다. 
이 대응 정보를 알고 있다면 보통의 독립 표본 t-검정에서 발생할 수 있는 
샘플간의 차이의 영향을 없앨 수 있기 때문에 특강 수강의 영향을 보다 정확하게 추정할 수 있다.
"""

# μ1=0 , μ2=0.5로 평균이 달라진 경우에 대해 대응 표본 t-검정을 실시해 보자.(N=5)
N = 5
mu1 = 0
mu2 = 0.5
np.random.seed(1)
x1 = sp.stats.norm(mu1).rvs(N)
x2 = x1 + sp.stats.norm(mu2, 0.1).rvs(N)
print(sp.stats.ttest_rel(x1, x2))
# Ttest_relResult(statistic=-7.1723380661732756, pvalue=0.0020008849290622677)



"""
카이 제곱 분산 검정 (Chi-Square Test for the Variance)


카이 제곱 분산 검정(Chi-Square Test for the Variance)은 
정규 분포의 샘플 분산 값은 정규화 하면 카이 제곱 분포를 따른다는 점을 이용하는 검정 방법이다.

그러나 SciPy는 카이 제곱 분산 검정에 대한 명령이 없으므로 chi2 클래스를 사용하여 직접 구현해야 한다.
"""


"""
문제1. 
A회사에서 제품을 생산하는데 분산은 25라고 알려져 있다.
그런데 불량률이 높아져서 분산이 25보다 크다는 의견이 나왔다.
실상을 파악하기 위해 표본 10개를 뽑아 조사했더니 표본 분산은 29가 나왔다고 한다.
이 때 분산이 25보다 크다고 할 수 있는지 유의수준 5%에서 검정하시오.
"""
div()

def chi_vartest(x, sigma2=25):
    v = 29
    t = (len(x)-1) * v / sigma2
    return t, 1-sp.stats.chi2(df=len(x)-1).sf(np.abs(t))

N = 10
mu = 0
sigma0 = np.sqrt(29)
x = sp.stats.norm(mu, sigma0).rvs(N)
print(x.std(), x.var())
# 5.38053269886 28.9501321235
print(chi_vartest(x))
# (5.428571428571429, 0.0010289842597944743)
# 귀무가설 기각. 작다고 할 수 있다.


"""
문제 2.
회사의 제품 분산은 7이다.
하지만 노력하여 7보다 작을꺼란 생각이 들었다. 
표본 20개를 뽑았더니 분산이 2가 나왔다고 한다.
이때 분산이 7보다 작다고 할 수 있는지 유의수준 1%에서 검정하시오.
"""
def chi_vartest(x, sigma2=7):
    s = 2
    t = (len(x)-1) * s / sigma2
    return t, 1-sp.stats.chi2(df=len(x)-1).sf(np.abs(t))

N = 20
sigma0 = np.sqrt(2)
x = sp.stats.norm(0, sigma0).rvs(N)
print(x.var(), x.std())
print(chi_vartest(x))



"""
등분산 검정 (Equal-variance test)

등분산 검정은 두 정규 분포로부터 생성된 두 개의 데이터 집합으로부터 
두 정규 분포의 분산 모수가 같은지 확인하기 위한 검정이다. 

가장 기본적인 방법은 F분포를 사용하는 것이지만 
실무에서는 이보다 더 성능이 좋은 bartlett, fligner, levene 방법을 주로 사용한다. 

scipy의 stats 서브패키지는 이를 위한 bartlett, fligner, levene 명령을 제공한다.
"""
div()

"""
문제1. 
동일한 제품 생산하는 기계1, 기계2가 있다.
분산은 동일한걸로 알려저있으나 최근 기계1에서 생산한 제품의 분산이 더 크다는 의견이 있다.
각각 표본 6개, 12개를 뽑아 조사하였더니 표본분산이 30, 8이 나왔다고 한다.
기계1의 분산이 더 크다고 할 수 있는지 유의수준 10%에서 검정.
"""
N1 = 6
N2 =12
var1 = 30
var2 = 8

x1 = np.random.normal(0, np.sqrt(var1), N1)
x2 = np.random.normal(0, np.sqrt(var2), N2)

print(x1.var(), x2.var())
# 22.8459677291 4.89569656862

# barlett 방법
print(sp.stats.bartlett(x1, x2))
# BartlettResult(statistic=4.7294436914832287, pvalue=0.029650474021736015)

# fligner 방법
print(sp.stats.fligner(x1, x2))
# FlignerResult(statistic=1.9124241466745544, pvalue=0.16669422899688607)

# levene 방법
print(sp.stats.levene(x1, x2))
# LeveneResult(statistic=2.0051214183470116, pvalue=0.17594151610660308)


"""
정규성 검정

회귀 분석 등에서는 
확률 분포가 가우시안 정규 분포를 따르는지 아닌지를 확인하는 것이 중요하다. 

이러한 검정을 정규성 검정(normality test)이라고 한다. 
정규성 분포 그 중요도 만큼 여러가지 검정 방법들이 개발되어 있으며 
scipy 패키지 이외에도 statsmodels 패키지에도 다양한 정규성 검정 명령어를 제공한다.

statsmodels에서 제공하는 정규성 검정 명령어

1. Omnibus Normality test
    statsmodels.stats.stattools.omni_normtest


2. Jarque–Bera test
    statsmodels.stats.stattools.jarque_bera

3. Kolmogorov-Smirnov test
    statsmodels.stats.diagnostic.kstest_normal

4. Lilliefors test
    statsmodels.stats.diagnostic.lillifors
    
    
scipy에서 제공하는 정규성 검정 명령어

1. Kolmogorov-Smirnov test
    scipy.stats.ks_2samp

2. Shapiro–Wilk test
    scipy.stats.shapiro

3. Anderson–Darling test
    scipy.stats.anderson

4. D'Agostino's K-squared test
    scipy.stats.mstats.normaltest

"""


x = sp.random.normal(0, 1, size=1000)
plt.hist(x)
plt.show()
print(sp.stats.shapiro(x))
# (0.9979338645935059, 0.25605106353759766) 귀무가설 채택. 정규성을 따른다.


# 이 중에서 Kolmogorov-Smirnov 검정은
# 사실 정규 분포에 국한되지 않고 두 샘플이 같은 분포를 따르는지 확인할 수 있는 방법이다.
np.random.seed(0)
N1 = 50
N2 = 100
x1 = sp.stats.norm(0, 1).rvs(N1)
x2 = sp.stats.norm(0.5, 1.5).rvs(N2)
print(sp.stats.ks_2samp(x1, x2))
# Ks_2sampResult(statistic=0.23000000000000004, pvalue=0.049516112814422863)
# 두 분포는 서로 다른 분포라고 할 수 있다.