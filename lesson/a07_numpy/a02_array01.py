'''
Created on 2017-07-25 10:10

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 arrray 처리
 
 1. 기본 형식
 array(list 형식)
 ex) np.array( [1, 2, 3] )
 
 2. type(basic_numpy 의 배열)
 numpy의 데이터 형식을 나타냄(basic_numpy.ndarray)
 
 3. 형식 : numpy배열이름.shape
 
 4. 데이터값 접근
    numpy배열이름[index]
    
    1) 1차원
    이름[index] ex) ar[0], ar[1]
    
    2) 2차원
    이름[상위index, 하위index]
    ex) br[0, 0], br[0, 1]
"""

import numpy as np


ar = np.array([1, 2, 3])
print(ar)

print(type(ar)) # <class 'using_numpy.ndarray'>

print(ar.shape) # (3,) : 1차원의 3개 data

print(ar[0], ar[1], ar[2])  # 1 2 3

# data 변경
ar[0] = 15
print(ar)  #  [15  2  3]

ar[0:2] = [15, 12] # 2개 이상 index data값 변경
print(ar) # [15 12  3]


"""
 2차원 배열 : array( [ [1, 2, 3], [4. 5. 6] ] )
                    1 2 : 차원 표시                
"""

br = np.array([ [1, 2, 3], [4, 5, 6] ])
print(br)
print(br.shape) # (2, 3) : 2차원 데이터, 각 배열 갯수 3개


"""
 ex)
 국어, 영어, 수학 점수를 데이터 할당
 총계와 평균처리
"""

kor = [50, 60, 70]
eng = [60, 75, 100]
math = [96, 65, 86]
score = np.array([kor, eng, math])
print(score)
print(type(score))  # <class 'using_numpy.ndarray'>
print(score.shape)  # (3, 3) : 3차원 데이터, 각 배열 갯수 3개

for i in score:
    print( "총계: {0} , 평균: {1}".format(sum(i), sum(i)/3) )
# 180 60.0
# 235 78.3333333333
# 247 82.3333333333


