'''
Created on 2017-07-25 16:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 index의 음수는 -1부터 시작해서 가장 뒤쪽으로부터 역순으로 처리.
 a = [1, 3, 5, 7]
 a[-1] = 7
 a[-3] = 3
 
 2차원 배열 접근 방법
 b = [[1, 2], [3, 4]]
 [첫번째 index, 두번째 index]
 b[0, 0] = 1
 b[1, 0] = 3
"""
import numpy as np

a = np.arange(1, 4)
print(a)
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[-1]:", a[-1])

b = np.array([[1, 2], [3, 4]])
print(b)
print("b[1,0]:", b[1, 0]) # 3
print("b[1][0]:", b[1][0])# 3
print("b[0]:", b[0])    # [1 2]
print("b[0, :]:", b[0, :])  # [1 2]
print("b[0][:]", b[0][:])   # [1 2]


# gabage값을 갖는 10행 5열의 배열 생성 : empty

a = np.empty((10, 5))
print(a)
print(a.ndim)
print(a.shape)

# 빈 배열에 데이터값 넣기
for idx in range(10):
    a[idx] = idx # 해당 index에 index를 element값으로 설정
print(a)

# 1, 3, 5, 7, 9행만 선택
b = a[[1, 3, 5, 7, 9], :]
print(b)

# [0, 3], [1, 4]만 선택
b = a[[0, 3], 1], a[[1, 4], 1]
print(np.array(b))