'''
Created on 2017-08-01 17:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
역행렬

정방 행렬에 대한 역행렬  inv(A)은 원래의 행렬 A와 다음 관계를 만족하는 정방 행렬을 말한다. 
inv(A) * A = A * inv(A) = I
I는 단위 행렬(identity matrix)이다.

역행렬의 성질

전치행렬의 역행렬은 역행렬의 전치행렬과 같다.
inv(A.T) = inv(A).T

두 개 이상의 정방 행렬의 곱은 마찬가지로 같은 크기의 정방행렬이 되는데
이러한 행렬의 곱의 역행렬에 대해서는 다음 성질이 성립한다.
inv(AB) = inv(B) * inv(A)
inv(ABC)=inv(C) * inv(B) * inv(A)

역행렬의 존재
행렬식의 값이 0이 아니면 역행렬이 존재한다. 
반대로 역행렬이 존재하면 행렬식의 값은 0이 아니다.

"""

"""
역행렬과 연립 방정식의 해

미지수의 수와 방정식의 수가 같다면 행렬  AA  는 정방 행렬이 된다.
만약 행렬  AA 의 역행렬  A−1A−1  이 존재한다면 역행렬의 정의에서 
연립 방정식의 해는 다음과 같이 구해진다.

Ax = b
inv(A)Ax = inv(A)b 
Ix = inv(A)b 
x = inv(A)b
"""

"""
numpy 역행렬 계산

numpy의 linalg 서브패키지에는 역행렬을 구하는 inv 라는 명령어가 존재한다. 
그러나 실제 계산시에는 수치해석 상의 여러가지 문제로 inv 명령어 보다는 
lstsq (least square) 명령어를 사용한다.
"""

A = np.array([1, 3, -2, 3, 5, 6, 2, 4, 3]).reshape(3, 3)
print(A)

b = np.array([[5], [7], [8]])
print(b)

print("===A의 행렬식===")

Adet = np.linalg.det(A)
print(Adet)

print("===A의 역행렬===")

Ainv = np.linalg.inv(A)
print(Ainv)

# x = inv(A) * b
div()

x = np.dot(Ainv, b)
print(x)

x = np.linalg.lstsq(A, b)
print(x)

div()
# A * x = b
x = np.dot(Ainv, b)

print(np.dot(A, x))

div()
# A * x - b =0
print(np.dot(A, x) - b)



"""
최소 자승 문제

다음으로 미지수의 수와 방정식의 수를 고려해 볼 때 연립 방정식에는 다음과 같은 세 종류가 있을 수 있다.
1. 방정식의 수가 미지수의 수와 같다. ( N=M )
2. 방정식의 수가 미지수의 수보다 적다. ( N<M )
3. 방정식의 수가 미지수의 수보다 많다. ( N>M )


최소 자승 문제의 답을 계산할 때는  A.T * A 가 항상 정방 행렬이 된다는 점을 이용한다. 
만약 정방행렬 A.T * A 의 역행렬  inv(A.T * A)이 존재한다면 다음과 같이 미지수 벡터  x 의 값을 구한다.

Ax ≈ b

이 식의 양변에  A.T를 곱하면 등식이 성립한다고 가정하자.
 A.T * Ax = A.T * b
 (A.T * A)x = A.T * b 
 x = inv(A.T * A) * A.T * b
 x = (inv(A.T * A) * A.T) *b
 
 여기서 inv(A.T * A) * A.T를 행렬  A의 의사 역행렬(pseudo inverse)
 라고 하며 다음과 같이  A+로 표기하기도 한다.
 A+ = inv(A.T * A) * A.T
 x = (A+)b
"""

# numpy의 lstsq 명령은 사실 이러한 최소 자승 문제를 푸는 명령이다.
div()
A = np.array([2, 0, -1, 1, 0, 2]).reshape(3, 2)
print(A)

b = np.array([[1], [0], [-1]])
print(b)

# A+ = inv(A.T * A) * A.T
Apinv = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
print(Apinv)

# x = (A+)b
x = np.dot(Apinv, b)
print(x)

print(np.linalg.lstsq(A, b))