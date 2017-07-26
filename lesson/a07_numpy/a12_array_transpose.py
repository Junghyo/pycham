'''
Created on 2017-07-26 11:10

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 행과 열의 전환
 
 1).T 전치행렬 : T라는 속성으로 기본 행과 열이 변환되어 처리된다.
 
 ex) a = array
     a.T
    
 
 2) transpose() 메서드

"""

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print(a)
# 1. 전치행렬 : .T
print(a.T)

# 2.transpose()
print(a.transpose()) # = a.T

# 2-1. transpose(1, 0), (0, 1)
print(a.transpose(1, 0)) # 전치행렬
print(a.transpose(0, 1)) # 원래행렬