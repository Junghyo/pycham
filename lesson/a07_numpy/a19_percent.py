'''
Created on 2017-07-26 14:55

@ product name : PyCharm Community Edition

@ author : yoda
'''

import numpy as np

a = np.array([90, 40, 30, 75])
# 상위에 소속된 데이터, 하위에 소속된 데이터 확인
print(len(a))  # 4
print("50%:", int((0.5 * len(a))))

# index 범위 데이터 접근. 배열[시작(0~):마지막(1~)]
print("1~2index:", a[0:2])

a.sort() # 오름차순 정렬
print("1~2index:", a[0:2])  # [30 40]

# 하위 50%
print("under 50% :", a[0:int(0.5 * len(a))])
# 상위 50%
print("over 50% :", a[int(0.5 * len(a)):])


"""
 ex)
 50명의 데이터를 임의로 0~100점까지 만들고
 이중 상위 10%, 상위 5% 데이터를 list
"""

score = np.random.random_integers(0, 100, 50)
print(score)
score.sort()
# 1. 상위 10%
print("상위 10% :", score[int(0.9 * len(score)):])
# 2. 상위 5%
print("상위 5% :", score[int(0.95 * len(score)):])

# 3. 하위 20%
print("하위 20% :", score[0:int(0.2 * len(score))])