'''
Created on 2017-07-26 12:10

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 abs() : 절대값
 
 sqrt() : 제곱근(root)
 
 square() : 제곱값

 modf() : 정수와 소수점 구분 2개 배열 반환
 
 sign() : 열 원소 부호 판별 함수(1 : pos, 2 : zero, -1 : neg)
 
 isnan() : not a number 포함 여부
 
 isfinite() : 유한수 포함 여부
 
 isinf() : 무한대 포함 여부
 
 logical_not() : 조건 만족하지 않을 경우 true 반환
"""

import numpy as np

a = np.array([1, 2, 5, 7, 10, 14, 3])

# boolean값으로 return 2보다 작거나 같으면 False 크면 True
print(np.logical_not(a <= 2))
print(a > 2)

# 해당 element값 확인
print(a[np.logical_not(a <= 2)])
print(a[a > 2])

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 2])

print(a + b)

# 조건에 의한 filter
stat = [True, False, False, True]

# np.where(조건, 배열1, 배열2)
print(np.where(a > b, a, b)) # True면 a의 element 반환, False이면 b의 element반환

"""
ex)
1학기 점수 : 70 80 90 60
2학기 점수 : 90 70 70 80

두 학기를 비교하여 높은 점수를 list 처리
"""
score1 = np.array([70, 80, 90, 60])
score2 = np.array([90, 70, 70, 80])

print(np.where(score1 > score2, score1, score2))

