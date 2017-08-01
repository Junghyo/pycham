'''
Created on 2017-08-01 16:03

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""

벡터와 행렬의 덧셈과 뺄셈
같은 크기를 가진 두개의 벡터나 행렬은 덧셈과 뺄셈을 할 수 있다. 
두 벡터와 행렬에서 같은 위치에 있는 원소에 대해 덧셈과 뺄셈을 하면 된다. 
이러한 연산을 요소별(element-wise) 연산이라고 한다.
"""
v1 = np.array([10, 11, 12, 13])
v2 = np.array([0, 1, 2, 3])
print(v1 - v2) # [10 10 10 10]

v1 = np.arange(1, 6).reshape(5, 1)
v2 = np.arange(10, 60, 10).reshape(5, 1)
print(v1 + v2)
# [[11]
#  [22]
#  [33]
#  [44]
#  [55]]


"""
 vector multiplation(내적)
 
 두 벡터의 곱셈을 하려면 다음과 같은 조건이 만족되어야 한다.
 우선 두 벡터의 길이가 같아야 하고
 앞의 벡터가 행 벡터이고 뒤의 벡터가 열 벡터여야 한다.
"""
div()
v1 = np.arange(1, 6)
v2 = np.array([10 for x in range(5)])
print(v1)
print(v2)
# 그냥 곱을 할 경우 각 element끼리 곱셈하여 return
print(v1 * v2)  # [10 20 30 40 50]
# 내적(dot)
print(np.dot(v1.T, v2)) # 150

v3 = np.array([1, 2, 3]).reshape(3, 1)
v4 = np.array([10, 10, 10]).reshape(3, 1)
print(np.dot(v3.T, v4)) # [[60]] scalar가 아닌 matrix로 표시


# 평균
div()
v2 = np.array([10 for x in range(5)])
print(v2) # [10 10 10 10 10]
print(v2.mean()) # 10

v3 = np.array([1, 2, 3]).reshape(3, 1)
print(v3)
print(v3.mean()) # 2.0

# 제곱합
print(np.sum(v3 * v3.T))


"""
 행렬의 곱셈(내적)
 axb 행렬과 cxd 행렬을 곱하면 axd행렬이 된다.
"""
a = np.array([[1, 2, 3], [4, 5, 6]]) # 2행 3열
b = np.arange(1, 7).reshape(3, 2) # 3행 2열
print(a)
print(b)
print(np.dot(a, b)) # 2행 2열이 된다.
print(np.dot(b, a)) # 3행 3열이 된다.

"""
 교환 법칙과 분배 법칙
 
 행렬의 곱셈은 곱하는 행렬의 순서를 바꾸는 교환 법칙이 성립하지 않는다. 
 그러나 덧셈에 대한 분배 법칙은 성립한다.
 
 1) AB와 BA는 다르다
 2) A(B+C) = AB+AC
 3) (A+B)C = AC+BC
"""
div()
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[2, 3], [4, 5]])

# AB 와 BA
print(np.dot(A, B))
# [[19 22]
#  [43 50]]
print(np.dot(B, A))
# [[23 34]
#  [31 46]]

# 다르다

# A(B+C) = AB + AC
print(np.dot(A, B+C))
# [[29 35]
#  [65 79]]
print(np.dot(A, B)+np.dot(A, C))
# [[29 35]
#  [65 79]]

# 같다

"""
 전치행렬 분배법칙
 (A+B).T = A.T + B.T
 (AB).T = B.T * A.T
"""
div()
print((A+B).T)
print(A.T + B.T)
# [[ 6 10]
#  [ 8 12]]

print(np.dot(A, B).T)
print(np.dot(B.T, A.T))
# [[19 43]
#  [22 50]]

"""
연속된 행렬의 곱셈은 계산 순서를 임의의 순서로 해도 상관없다.

ABC=(AB)C=A(BC)
ABCD=((AB)C)D=(AB)(CD)=A(BCD)=A(BC)D
"""
div()

a = np.array([1, 2])
b = np.array([[1, 2], [3, 4]])
c = np.array([[5], [6]])
print(np.dot(np.dot(a, b), c)) # (AB)C : 95
print(np.dot(a, np.dot(b, c))) # A(BC) : 95

# 단위행렬의 곱셈 : AI = IA = A
a = np.arange(1, 10).reshape(3, 3)
i = np.eye(3)
print(np.dot(i, a))



# 이차형식 X.T * A * X  : 행벡터 x 정방 행렬 x 열벡터
div()
X = np.arange(1, 4).reshape(3, 1)
A = np.arange(1, 10).reshape(3, 3)
print(X.T)
print(A)
print(X)
print(np.dot(np.dot(X.T, A), X))