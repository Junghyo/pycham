'''
Created on 2017-07-26 13:08

@ product name : PyCharm Community Edition

@ author : yoda
'''

import numpy as np

a = np.random.randint(1, 10, 10)
print(a)
a.sort()
print(a) # 오름차순으로 정렬


a = np.random.random_integers(1, 20, 9).reshape(3, 3)
print(a)

# axis 0 : 열단위로 element를 비교하여 정렬
# axis 1 : 행단위로 element를 비교하여 정렬

# a.sort(axis=0) # 열단위로 정렬
# print(a)

a.sort(axis=1) # 행단위로 정렬
print(a)

"""
 ex)
1-1 2명
1-2 2명
2-1 2명
2-2 2명
3-1 2명
3-2 2명

위 데이터를 2차원 배열로 만들기
1. 학년별 한반편성 하기
2. 반별로 반편성을
1-1, 2-1, 3-1
"""
print("=" * 50)
one_one = ["1_1stu1", "1_1stu2"]
one_two = ["1_2stu1", "1_2stu2"]
two_one = ["2_1stu1", "2_1stu2"]
two_two = ["2_2stu1", "2_2stu2"]
three_one = ["3_1stu1", "3_1stu2"]
three_two = ["3_2stu1", "3_2stu2"]
school = np.array([one_one, one_two, two_one, two_two, three_one, three_two])
print("===학교 학급===")
print(school)

# 1.학년별 한반편성
print("===학년별 한반편성===")
school_spl = np.array(np.split(school, 3, axis=0))
i = 1
for x in school_spl:
    print("{0}학년: {1}" .format(i, x.flatten()))
    i += 1

# 반별로 반편성을 1-1, 2-1, 3-1
print("===반별로 반편성을 1-1, 2-1, 3-1===")
one = school_spl[0].flatten()
two = school_spl[1].flatten()
three = school_spl[2].flatten()

school_re = np.array([one, two, three])
print(school_re)

