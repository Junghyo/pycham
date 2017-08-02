'''
Created on 2017-08-02 18:11

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
stack()
1. DataFrame에서 컬럼을 하위 인텍스로 해서 Series를 생성
2. NaN 데이터 제외
3. dropna에 False 대입 

unstack()
1. Series(계층적인덱스) ==> DataFrame(하위레벨 인덱스)  
2. DataFrame인 경우는 컬럼을 상위 인덱스로 하는 Series 객체
"""
stock1={'2017-08-01':[84900,1756,292000],
        '2017-08-02':[86100,np.nan,295000]}

# DataFrame
df1 = pd.DataFrame(stock1, index=['다음','넥슨','NC'])
print(df1)

# stack
div()
print(df1.stack())
print(type(df1.stack())) # <class 'pandas.core.series.Series'>

# unstack
div()
print(df1.unstack())
print(type(df1.unstack())) # <class 'pandas.core.series.Series'>
