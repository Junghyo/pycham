'''
Created on 2017-07-25 12:58

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 ndarray의 자료형
 
 dtype을 통해서 데이터의 형태를 casting, promote 변경 및 설정 가능
 또는 해당 데이터의 type을 확인할 수 있다.
 
 astype()을 이용하여 type 변경 가능

 정수형 : int8, int16, ....., uint8
 
 실수형 : float16, float32, ....
 
 복소수 : complex64, complex128
 
 boolean : bool
 
 객체 : object
"""

import numpy as np

# data type check : dtype
i = np.array([1, 2, 3])
print("type:", i.dtype) # type: int32

s = np.array(["hi", "hello", "nice"])
print("type:", s.dtype) # type: <U5

s = np.array(["안녕", "에이스", "호날두"])
print("type:", s.dtype) # type: <U3

s = np.array(["12", "34", "55"])
print("type:", s.dtype) # type: <U2

f = np.array([3, 2.9, 3.14, -31])
print("type:", f.dtype) # type: float64

t = np.array(["3", 2.8, 3])
print("type:", t.dtype) # <U3

# 문자열 data를 int32로 casting하여 처리
c = np.array(["3", 3, 3.5], dtype=np.int32)
print("type:", c.dtype)  # type: int32


# astype(변수명, 변경할데이터type)
# 해당 변수를 변경할 데이터type으로 바꾸는 기능

ast = t.astype(np.string_)
print("type:", ast.dtype)   # type: |S3


"""
 ex)
 1. 5~20까지 문자형으로 선언하고 선언된 data를
    int32로 변경 및 합산 처리
 
 2. 문자형으로 변환해서 5678....20으로 출력
"""
print("=" * 50)
ex = np.array([str(i) for i in range(1, 21)])
print(ex)

# 현재 type 문자형
print("type:", ex.dtype )   # type: <U2

# 숫자형으로 변경(int32)
ex = np.array([str(i) for i in range(1, 21)], dtype=np.int32)
print("type:", ex.dtype)    # type: int32
print(sum(ex))  # 210

# 다시 문자형으로 변경
ex_s = ex.astype(np.str)
print("type:", ex_s.dtype)  # type: <U11

# 문자형으로 변환해서 5678....20으로 출력
print(ex_s)
print(str.join("", ex_s))