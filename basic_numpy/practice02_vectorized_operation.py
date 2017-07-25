'''
Created on 2017-07-25 18:08

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 vectorlized operation
 
"""
import numpy as np

# 만약 벡터화 연산을 사용하지 않는다면?
x = np.arange(1, 1001)
y = np.arange(1001, 2001)
z = np.zeros_like(x)

for i in range(1000):
    z[i] = x[i] + y[i]

print(z[:10])

# 하지만 벡터화 연산을 사용한다면
z1 = x + y
print(z1[:10])


# 비교도 가능하다

a = np.array([1, 3, 3, 4, 7])
b = np.arange(1, 6)
print(a == b)    #[ True False  True  True False]

print(a >= b)