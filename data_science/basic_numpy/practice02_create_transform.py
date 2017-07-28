'''
Created on 2017-07-25 14:33

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 numpy 배열의 생성과 변형
 
 numpy의 자료형은 dtype이라는 인수로 지정
 
 dtype 접두사	    설명	            사용 예
 t	                비트 필드	    t4 (4비트)
 b	                불리언	        b (참 혹은 거짓)
 i	                정수	            i8 (64비트)
 u	                부호 없는 정수	u8 (64비트)
 f	                부동소수점	    f8 (64비트)
 c	                복소 부동소수점	c16 (128비트)
 O	                객체	            0 (객체에 대한 포인터)
 S, a	            문자열	        S24 (24 글자)
 U	                유니코드 문자열	U24 (24 유니코드 글자)
 V	                기타          	V12 (12바이트의 데이터 블럭)
 
"""
import numpy as np

# ndarray 객체의 dtype 속성으로 자료형을 알 수 있다.
x = np.arange(1, 4)
print(x)
print(x.dtype) # int32

# 만약 부동소수점을 사용하는 경우, 무한대를 표현하기 위한 np.inf와
# 정의할 수 없는 숫자를 나타내는 np.nan을 사용할 수 있다.
print(np.exp(-np.inf))     # 0.0
# print(np.array([1, 0]) / np.array([0, 0])) # [ inf  nan]


"""
 배열 생성
 
    zeros, ones
    zeros_like, ones_like
    empty
    arange
    linspace, logspace
    rand, randn
"""
print("=" * 50)
print("배열 생성")
print("=" * 50)


# zeros() : 크기가 정해져 있고 모든 값이 0인 배열 생서
a = np.zeros(5)
print(a)     # [ 0.  0.  0.  0.  0.]
print(a.ndim) # 1차원

# dtype 을 명시하면 해당 data type의 원소를 가진 배열을 생성
# 5행, 2열 f8 type 배열 생성
b = np.zeros((5, 2), dtype="f8")
print(b)
print(b.dtype)  # float64

c = np.zeros(5, dtype="S4")
c[0] = "abcd"
c[1] = "ABCDEFGHI"
print(c)    # [b'abcd' b'ABCD' b'' b'' b'']
print(c.dtype)  # |S4 type의 데이터 크기 제한을 넘어서서 문자열이 잘림

# ones() : 0이 아닌 1로 초기화된 배열 생성
# 2면, 3행, 4열 1로 초기화된 배열 생성 data type은 i8
a = np.ones((2, 3, 4), dtype="i8")
print(a)
print(a.ndim) # 3차원
print(a.shape) # 2, 3, 4
print(a.dtype) # int64

# 배열 크기를 tuple로 지정하지 않고 특정 배열 혹은 list와 같은 크기를 생성하고 싶으면
# ones_like(), zeros_like() 이용
e = range(10)
print(e)    # range(0, 10) 0 ~ 9
a = np.ones_like(e, dtype="f")
print(a)    # [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
print(a.dtype)  # float32

# 배열의 크기가 커지면 배열을 초기화하는데도 시간이 걸린다.
# 시간 단축을 위해 생성만 하고 초기화는 하지 않는 empty()를 사용
# 어떤 값이 포함될지는 알 수가 없다.(random 생성)
g = np.empty((4, 3))
print(g)

# 범위를 정하고 특정한 규칙(간격)에 따라 배열 생성 : arange()

# 끝만 명시 : 0부터 시작
print(np.arange(10)) # 0 ~ 9

# 시작, 끝(포함하지않음), 단계(간격)
print(np.arange(start=3, stop=21, step=2))

# linspace(), logspace() : 선형 구간, 로그 구간을 지정한 구간의 수만큼 분할

# linspace(시작, 끝(포함), 갯수)
print(np.linspace(start=0, stop=100, num=5))    # [   0.   25.   50.   75.  100.]
print(np.linspace(start=0, stop=100, num=5, endpoint=False)) # [  0.  20.  40.  60.  80.]

# endpoint=False 끝값을 포함하지 않음

# logspace()
print(np.logspace(start=0, stop=4, num=4))
# [  1.00000000e+00   2.15443469e+01   4.64158883e+02   1.00000000e+04]
print(np.logspace(start=0, stop=4, num=4, endpoint=False))
# [    1.    10.   100.  1000.]


# 임의의 난수를 생성하고 싶다면 rand(), randn()
# rand() : uniform 분포를 따르는 난수 생성
# randn() : 가우시안 정규분포를 따르는 난수 생성
# seed() : 난수 고정 시 사용
print(np.random.rand(4))  # seed 전. run 할 때마다 값이 바뀜
np.random.seed(0) # seed 고정
print(np.random.rand(4)) # seed 후. 값이 고정되어 변하지 않는다

# 3행 5열 난수 만들기
a = np.random.rand(3, 5)
print(a)

# 3행 3열 난수 만들기
b = np.random.randn(3, 3)
print(b)

# 전치행렬 연산(transpose) # 행의 값들이 열로 바뀌고 열의 값들이 행으로 바뀜
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(a.T)

a = np.arange(1, 7).reshape(2, 3)
print(a)
print(a.T)

print("=" * 50)

# 배열의 크기 변형
a = np.arange(12)
print(a)
print(a.ndim)   # 1
print(a.shape)  # (12,) 12행

a1 = a.reshape(3, 4)
print(a1)
print(a1.ndim)   # 2
print(a1.shape) # 3행 4열

# reshape(면, 행, 렬)
a2 = a.reshape(2, -1) # 2행, -1을 넣으면 element 길이를 계산하여 알맞게 만들어줌
print(a2) # 2행 6열로 됨

a3 = a.reshape(3, 2, 2) # 3면, 2행, 2열로 변형
print(a3)

# 다차원 배열을 1차원으로 펼치려면 flatten() 사용
print(a3.flatten())

"""
 1~6 element들의 행렬
 
 각각 다르니 반드시 주의해야 한다.

"""
# 길이가 6인 1차원 행렬
print("=" * 50)
print("1차원 행렬")
print("=" * 50)


x = np.arange(1, 7)
print(x)
print("[0]:", x[0])
print("ndim:", x.ndim)
print("shape:", x.shape)
print("len:", len(x))


# 1행 6열 2차원 행렬
print("=" * 50)
print("1행 6열 2차원 행렬")
print("=" * 50)


x1 = x.reshape(1, 6)
print(x1)
print("[0]:", x1[0])
print("ndim:", x1.ndim)
print("shape:", x1.shape)
print("len:", len(x1))


# 6행 1열 2차원 행렬
print("=" * 50)
print("6행 1열 2차원 행렬")
print("=" * 50)

x2 = x1.reshape(6, 1)
print(x2)
print("[0]:", x2[0])
print("ndim:", x2.ndim)
print("shape:", x2.shape)
print("len:", len(x2))


# 2면 1행 3열 3차원 행렬
print("=" * 50)
print("2면 1행 3열 3차원 행렬")
print("=" * 50)

x3 = x2.reshape(2, 1, 3)
print(x3)
print("[0]:", x3[0])
print("ndim:", x3.ndim)
print("shape:", x3.shape)
print("len:", len(x3))

# 3면 2행 1열 3차원 행렬
print("=" * 50)
print("3면 2행 1열 3차원 행렬")
print("=" * 50)

x4 = x3.reshape(3, 2, 1)
print(x4)
print("[0]:", x4[0])
print("ndim:", x4.ndim)
print("shape:", x4.shape)
print("len:", len(x4))


# 차원만 1차원 증가 시키기
# newaxis 사용
print("=" * 50)
print("newaxis 사용")
print("=" * 50)

x5 = x[:, np.newaxis]
print(x5)
print("[0]:", x5[0])
print("ndim:", x5.ndim)
print("shape:", x5.shape)
print("len:", len(x5))

x5_1 = x1[:, np.newaxis]
print(x5_1)
print("[0]:", x5_1[0])
print("ndim:", x5_1.ndim)
print("shape:", x5_1.shape)
print("len:", len(x5_1))

x6 = x4[:, np.newaxis]
print(x6)
print("[0]:", x6[0])
print("ndim:", x6.ndim)
print("shape:", x6.shape)
print("len:", len(x6))

"""
 배열 연결
 
 행의 수나 열의 수가 같은 두 개 이상의 배열을 연결하여(concatenate)
 더 큰 배열을 만들 때는 다음과 같은 명령을 사용한다.
 
 hstack
 vstack
 dstack
 stack
 r_
 c_
 tile
 
"""


# hstack() : 행의 수가 같은 두 개 이상의 배열을 옆으로 연결하여 열의 수를 증가
print("=" * 50)

a = np.ones((2, 3))
b = np.zeros((2, 2))
print(a)
print(b)
print(np.hstack([a, b]))


# vstack() : 열의 수가 같은 두 개 이상의 배열을 위아래로 연결하여 형의 수를 증가
print("=" * 50)

a = np.ones((3, 3))
b = np.zeros((1, 3))
print(a)
print(b)
c = np.vstack([a, b])
print(c)
print("[0]:", c[0])
print("ndim:", c.ndim)
print("shape:", c.shape)
print("len:", len(c))

# dstack() : 깊이(depth) 방향으로 배열을 합친다. 가장 안족의 원소의 차원이 증가.
# 3행 4열 을 2개 합치면 ===> 3면 4행 2열
print("=" * 50)

a = np.arange(1, 13).reshape(3, 4)
b = np.arange(13, 25).reshape(3, 4)
c = np.dstack([a, b])
print("=== a ===")
print(a)
print("=== b ===")
print(b)
print("=== c ===")
print(c)
print("[0]:", c[0])
print("ndim:", c.ndim)
print("shape:", c.shape)
print("len:", len(c))

# === a ===
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# === b ===
# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]

# === c ===
# [[[ 1 13]
#   [ 2 14]
#   [ 3 15]
#   [ 4 16]]
#
#  [[ 5 17]
#   [ 6 18]
#   [ 7 19]
#   [ 8 20]]
#
#  [[ 9 21]
#   [10 22]
#   [11 23]
#   [12 24]]]
# [0]: [[ 1 13]
#  [ 2 14]
#  [ 3 15]
#  [ 4 16]]


"""
 stack()
 
 stack 명령은 지정한 차원(축으로) 배열을 연결한다.
 axis 인수(디폴트 0)를 사용하여 연결후의 회전 방향을 정한다.
 디폴트 인수값은 0이고 가장 앞쪽에 차원이 생성된다. 
 즉, 배열 두 개가 겹치게 되므로 연결하고자 하는 배열들의 크기가 모두 같아야 한다.
 
 3행 4열 2개 열결 => 2면 3행 4열
 
"""
# axis가 0일 경우
print("=" * 50)

c = np.stack([a, b])
print(c)
print(c.shape)  # (2, 3, 4)

print("=" * 50)

d = np.stack([a, b], axis=1)
print(d)
print(d.shape)  # (3, 2, 4)

print("=" * 50)

e = np.stack([a, b], axis=2)
print(e)
print(e.shape)  # (3, 4, 2)

# axis = 3 이상은 error

"""
 r_
 
 중요 : 1차원일 경우에는 좌우로 연결
 
 vstack 명령과 비슷하게 배열을 상하로 연결한다.
 다만 메서드임에도 불구하고 소괄호(parenthesis, ())를 사용하지 않고
 인덱싱과 같이 대괄호(bracket, [])를 사용한다.
 이런 특수 메서드를 인덱서(indexer)라고 한다.
 
 c_
 
 hstack과 비슷하게 좌우(옆)으로 연결

"""

# 1차원일 경우
print("=" * 50)

d = np.array([1,2,3])
e = np.array([4,5,6])

f = np.r_[d, e]
print(f)
print(f.ndim)
print(f.shape)

f = np.c_[d, e]
print(f)
print(f.ndim)
print(f.shape)

f = np.hstack([d, e])
print(f)

f = np.vstack([d, e])
print(f)

a = np.arange(1, 5).reshape(2, 2)
b = np.arange(5, 9).reshape(2, 2)

print("=" * 50)
print("_r")
print("=" * 50)

c = np.r_[a, b]
print(c)


print("=" * 50)
print("vstack")
print("=" * 50)

c = np.vstack([a, b])
print(c)


print("=" * 50)
print("_c")
print("=" * 50)

c = np.c_[a, b]
print(c)


print("=" * 50)
print("hstack")
print("=" * 50)

c = np.hstack([a, b])
print(c)

# tile : 동일한 배열을 반복하여 연결
print("=" * 50)

print(a)

b = np.tile(a, 2) # 열로 2번 반복
print(b)

b = np.tile(a, (3, 3)) # 행으로 3번 열로 3번 반복
print(b)

"""
 grid 생성
 
 변수가 2개인 2차원 함수의 그래프를 그리거나 표를 작성하려면 많은 좌표를
 한꺼번에 생성하여 각 좌표에 대한 함수 값을 계산해야 한다.
 예를 들어 x, y 라는 두 변수를 가진 함수에서 x가 0부터 2까지,
 y가 0부터 4까지의 사각형 영역에서 변화하는 과정을 보고 싶다면
 이 사각형 영역 안의 다음과 같은 (x,y) 쌍 값들에 대해 함수를 계산해야 한다.
 
 (x,y)=(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),⋯(2,4)
 
 이러한 과정을 자동으로 해주는 것이 numpy의 meshgrid
 단 조합이 된 (x,y)쌍을 x값만을 표시하는 행렬과 
 y값만을 표시하는 행렬 두 개로 분리하여 출력한다.
"""
print("=" * 50)
print("grid")
print("=" * 50)

x = np.arange(3)
y = np.arange(5)
print(x)
print(y)
X, Y = np.meshgrid(x, y)
print("=== X ===")
print(X)
print("=== Y ===")
print(Y)
xy = [tuple(zip(x, y)) for x, y in zip(X, Y)]
print(xy)

import matplotlib.pyplot as plt
plt.scatter(X, Y, linewidths=10)
plt.show()