'''
Created on 2017-08-01 17:08

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

# 행렬의 부호
# 이차형식 X.T * A * X  : 행벡터 x 정방 행렬 x 열벡터
# X.T * A * X > 0 : 양 한정(positive definite)
# X.T * A * X >= 0 : 양-반한정(positive semi-definite)
# 단위행렬 : 양-한정
X = np.array([-3, 5]).reshape(1, 2)
I = np.eye(2)
print(np.dot(np.dot(X, I), X.T)) # [[ 34.]]

# 다음 행렬의 부호는?
X = np.array([13, -5]).reshape(1, 2)
A = np.array([1 for i in range(4)]).reshape(2, 2)
print(np.dot(np.dot(X, A), X.T))
# 양-한정

"""
행렬의 크기

부호와 마찬가지로 행렬의 크기를 정의하는 것도 어렵다. 
하지만 하나의 행렬에 대해 
하나의 실수를 대응시키는 놈(norm), 대각 성분(trace), 행렬식(determinant)이란 연산은 
행렬의 크기와 비슷한 의미를 가진다.
"""

# 행렬 norm
# numpy에서는 linalg 서브패키지의 norm 명령으로 행렬의 놈을 계산할 수 있다.
div()
a = (np.arange(9)-4).reshape(3, 3)
print(a)
# [[-4 -3 -2]
#  [-1  0  1]
#  [ 2  3  4]]

print("행렬 a의 norm :", np.linalg.norm(a))
"""
 trace
 
 대각 성분(trace)은 정방 행렬에 대해서만 정의되며 대각 원소들의 합으로 계산된다.
 tr(cA)=ctr(A) 
 tr(A.T)=tr(A) 
 tr(A+B)=tr(A)+tr(B) 
 tr(AB)=tr(BA) 
 tr(ABC)=tr(BCA)=tr(CAB)
"""
print("행렬 a의 trace :", np.trace(a))

"""
 행렬식
 정방 행렬  A 의 행렬식(determinant)은  
 det(A) 라는 기호 또는  |A| 라는 기호로 표기한다.
 
 1×1 행렬의 행렬식 : det([a])=a
 
 2×2 행렬의 행렬식 : ad - bc
 [[ a  b]
  [ c  d]] 
  
 3×3 행렬의 행렬식 : aei+bfg+cdh−ceg−bdi−afh
 [[ a  b  c]
  [ d  e  f]
  [ g  h  i]]
  
  행렬식은 다음과 같은 성질을 만족한다.

1. 전치행렬의 행렬식은 원래의 행렬의 행렬식과 같다.
det(A.T)=det(A)
 
2. 단위 행렬의 행렬식은 1이다.
det(I)=1
 
두 행렬의 곱의 행렬식은 각 행렬의 행렬식의 곱과 같다.
det(AB)=det(A)det(B)
 
역행렬의 행렬식은 원래의 행렬의 행렬식 값이 역수와 된다. (역행렬에 대해서는 곧 설명한다.)
det(Ainv)=1/det(A)
"""
# numpy에서는 linalg 서브패키지의 det 명령으로 행렬식을 계산할 수 있다.
print("행렬 a의 det:", np.linalg.det(a))
b = np.arange(1, 5).reshape(2, 2)
print(np.linalg.det(b))
