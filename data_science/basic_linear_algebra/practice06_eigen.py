'''
Created on 2017-08-02 11:46

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
고유값


numpy linalg 서브패키지에서는 고유값과 고유벡터를 구할 수 있는 eig 명령을 제공한다. 
고유값은 벡터의 형태로, 
고유벡터는 고유벡터행렬의 형태로 

묶여서 나오면 고유벡터는 크기가 1되도록 이 정규화가 되어있다.
"""

A = np.array([[1, 3], [4, 2]])
# 고유값
value = np.linalg.eigvals(A)
print(value)

# 고유벡터
value, vector = np.linalg.eig(A)
print(value)
print(vector)