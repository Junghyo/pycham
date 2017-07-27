'''
Created on 2017-07-27 11:16

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 numpy에서 저장과 열기
 
 1. numpy.save(파일경로, 데이터) : row 데이터 형태로 저장, 확장자는 .npy 자동으로 생성
 
 2. 불러오기 : load(파일경로)
 
 3. dict 형태(key=value, key=value)로 저장
    numpy.savez("파일명", key명=데이터, key명=데이터)저장 (확장자.npz)

 4. 데이터 불러올 시, 데이터명["key"]
 
 5. 구분자로 csv형식 파일 읽기
    loadtxt("파일경로", delimiter="구분자") csv 형식의 파일 읽기
    
"""

import numpy as np
a = [100, 200, 300]

# save : numpy.save()  .npy
np.save("z01_data01", a)

# read : load()
b = np.load("z01_data01.npy")
print("load data :", b)

c = a + b
# dict 형식으로 저장
# save : numpy.savez()  .npz
np.savez("z02_dict", a=a, b=b, c=b)

# read : load()
result = np.load("z02_dict.npz")
print(result)
print(result["a"])
print(result["b"])
print(result["c"])
print(result.keys())
print(result.items())

"""
ex)
3명의 급여 데이터가 있다.
1월 급여 데이터: 300, 400, 500
1. 1월 급여 저장
2. 1월 급여 데이터 로딩
3. 2월 급여 = 1월 급여 + 보너스 15%
4. 2월급여 dict 형식으로 저장
5. 세번째사람 급여 로딩
"""
from mymod.print import *
div()
# 1월 급여 저장
sal1 = [300, 400, 500]
np.save("z03_sal1", sal1)

# 1월 급여 로딩
result1 = np.load("z03_sal1.npy")
print(result1)

# 2월 급여 설정
sal2 = result1 + result1 * 0.15
print(sal2)

# 2월 최종급여 dict형식 저장
np.savez("z03_sal2", p1=sal2[0], p2=sal2[1], p3=sal2[2])

result2 = np.load("z03_sal2.npz")
print(result2["p3"])