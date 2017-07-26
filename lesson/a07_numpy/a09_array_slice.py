'''
Created on 2017-07-26 09:42

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 slicing
 
 1. 복제가 되지 않음
 2. 복제가 필요한 경우 copy() 호출 처리
 3. 형태: [시작위치:마지막위치]
    2차원 이상 [행의 slicing, 열의 slicing]
"""
import numpy as np

a = np.arange(1, 6)
b = a[0:3]

print(a)     # [1 2 3 4 5]
print(b)

c = a[0:3].copy()

print(b)    # [1 2 3]
print(c)    # [1 2 3]

a[0] = 10

print(a)    # [10  2  3  4  5]
print(b)    # [10  2  3]
print(c)    # [1 2 3]

# a[0] element를 변경했더니 b[0]도 변경되었지만
# copy()를 사용해서 만든 array c에는 영향을 주지 않음

b[0] = 11

print(a)     # [11  2  3  4  5]
print(b)     # [11  2  3]
print(c)     # [1 2 3]

# slicing하여 복제한 b[0]을 변경해도 a[0]에 영향을 미침


# slicing한 array에는 기존데이터가 변경한 경우에 영향을 미친다.
# 변경된 내용을 독립적으로 활용하기 위해서는 copy()를 통해 처리해야함

# 배열명[index : ] : 해당 index 이후에 마지막까지 내용을 처리함
d = a[-2:]

print(a)
print(d)    # [4 5]