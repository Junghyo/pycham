'''
Created on 2017-07-26 11:04

@ product name : PyCharm Community Edition

@ author : yoda
'''

import numpy as np

a = np.arange(20).reshape(5, 4)
print(a)

# 2행, 3행 선택하기
print("2행, 3행 선택하기")
print(a[[1, 2], ])


# 뒤에서 2개행 선택
print("뒤에서 2개행 선택")
print(a[-2:, ])

# 1, 3, 5행  1, 3열 선택
print("1, 3, 5행  1, 3열 선택")
print(a[[0, 2, 4]][:, [0, 2]])
# ix_ : 보다 효과적으로 선택 처리
# ix_([행의 index], [열의 index])
print(a[np.ix_([0, 2, 4], [0, 2])])