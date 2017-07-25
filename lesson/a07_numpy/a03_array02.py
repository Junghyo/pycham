'''
Created on 2017-07-25 11:00

@ product name : PyCharm Community Edition

@ author : yoda
'''
import numpy as np

## 1차 배열(vector) 생성
ar = np.array([1, 2, 3])
print(ar)

br = np.array([ [1, 2, 3], [5, 6, 7] ])
print(br)

# arrange(시작, 마지막) 으로 해당 크기의 배열을 만듦
# arrange(크기) 0부터 크기만큼의 배열을 생성

ar1 = np.arange(10) # 0 ~ 9
print(ar1)  # [0 1 2 3 4 5 6 7 8 9]

# 범위를 지정하고, 범위 내에 같은 간격의 데이터를 설정
# linspace(start, end, 갯수)

ar2 = np.linspace(0, 1, 6)  # 0 ~ 1 까지 6개의 배열 만들기
print(ar2) # [ 0.   0.2  0.4  0.6  0.8  1. ]

# 마지막 값에 대한 옵션 endpoint = False  : 마지막값은 포함하지 않는다.
ar = np.linspace(0, 1, 6, endpoint=False)
print(ar)   # [ 0.          0.16666667  0.33333333  0.5         0.66666667  0.83333333]

# 변형되는 배열 만들기 : reshape
# reshape(1차원 갯수, 2차원 갯수, ....) : 해당하는 차원의 데이터 형태로 변경
ar = np.arange(10)
print(ar)                   # [0 1 2 3 4 5 6 7 8 9]
ar_r = ar.reshape(2, 5)            # 2차원, 각배열 5개의 데이터로 변경
print(ar_r)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]


"""
 ex)
 1. 빵이 10개가 있다. 곰돌이 3마리가 나누어서 가질 갯수를 linespace를 통해 나타나세요.
"""
bread = np.linspace(1, 10, 3)
print(bread)

"""
 ex)
 2. 학생 3명의 국어, 영어, 수학 점수 9개를 list로 만든 후, 3행 3열의 2차원 배열로 list해서 점수를 나타내세요
"""
import random
i = 1
score = []
while i < 10:
    score.append(random.randint(0, 100))
    print(i)
    i += 1

print(score)
np_score = np.array(score)
print(np_score.reshape(3, 3))