'''
Created on 2017-07-26 13:00

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 split()
 
 array를 여러 개의 크기로 나누어 주는 함수
 나누는 기준에 따라 axis의 속성으로 X, Y축에 0, 1 값을 할당
"""

import numpy as np

a = np.arange(1, 17).reshape(4, 4)
print(a)

# split(나눌배열, 나울갯수, axis=0/1)
# 가로 방향으로 4개로 나눔
a_split = np.split(a, 4, axis=0)

print("가로 방향으로 4개 나누기")
i = 1
for x in a_split:
    print("{0} 번째:{1} ".format(i, x))
    i += 1

# 세로 방향으로 2개로 나눔
i = 1
a_split = np.split(a, 2, axis=1)
print("세로 방향으로 2개 나누기")
for x in a_split:
    print("{0} 번째:{1} ".format(i, x))
    i += 1
