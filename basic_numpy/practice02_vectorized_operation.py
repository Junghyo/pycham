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
c = np.arange(1, 6)
print(a == b)    #[ True False  True  True False]

print(a >= b)

# 만약 배열 전체를 비교하고 싶다면 all을 사용한다
print(np.all(b == c)) # True
print(np.all(a > b))  # False

# 지수 함수, 로그 함수 등의 수학 함수도 벡터화 연산을 지원한다.
a = np.arange(5)
print(np.exp(a)) # 지수 함수
# print(np.log(a)) # 로그 함수
print(10 ** a)
# print(np.log10(a))

print(np.log10(10))  # 1

"""
연습 문제 1

벡터 x가 다음과 같을 때, 여러가지 수식을 사용하여 같은 크기의 벡터 y를 만든다.

x = np.arange(10)
"""
x = np.arange(10)
y = x
print(y)
z = np.linspace(1, 10, 10
                )
print(z)