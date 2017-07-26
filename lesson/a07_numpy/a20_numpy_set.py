'''
Created on 2017-07-26 15:36

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 집합관련함수
 
 unique() : 중복제거
 
 intersectId() : 교집합
 
 nionId() : 합집합
 
 inId() : 데이터의 존재 여부 boolean
 
 setdiffId() : 차집합
 
 sectxorId() : 한쪽에만 있는 데이터 집합
"""

import numpy as np

a = np.random.random_integers(1, 7, 5)
print(a)

# 중복제거
print(np.unique(a))

b = np.random.random_integers(3, 12, 5)
print(b)

# 교집합
print(np.intersect1d(a, b))

# 합집합
print(np.union1d(a, b)) # 중복은 하나만 적용

# 데이터 존재여부
print(np.in1d(a, b)) # a의 데이터가 b에 존재하는지 boolean값으로 return

# 차집합
print(np.setdiff1d(a, b)) # a - b

# 한쪽에만 있는 데이터 집합
print(np.setxor1d(a, b))