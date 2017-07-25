'''
Created on 2017-07-25 11:43

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 using using_numpy array
 
 array
 1. 모든 원소가 같은 자료형이어야 한다.
 2. 원소의 갯수를 바꿀 수 없다.
"""

### using_numpy package import
import numpy as np

"""
 1. 1차원 배열 만들기
"""
print("=" * 50)
print("1. 1차원 배열 만들기")
print("=" * 50)


a = np.array( [ i for i in range(0, 10)] )
print(a)        # [0 1 2 3 4 5 6 7 8 9]
print(type(a))  # <class 'numpy.ndarray'>
print(a.ndim) # 1차원

"""
 2. vectorized operation
"""
print("=" * 50)
print("2. vectorized operation")
print("=" * 50)


# ex1) array a의 원소에 2를 곱하여 새로운 list만들기 : using for loop
b = []
for data in a:
    b.append(data * 2 )

print(b)

# ex2) using vectorized operation

print(type(b))  # <class 'list'>
d = b * 2
print(d)
# list를 2번 곱하면 해당 원소에 x2가 되는게 아니라 같은 원소가 2번 반복

# 백터화 연산 사용
a2 = a * 2
print(a2)   # [ 0  2  4  6  8 10 12 14 16 18]
print(type(a2)) # <class 'numpy.ndarray'>

# vectorized operation은 모든 종류의 수학 연산 적용 가능
a = np.array( [i for i in range(1, 4)] )
b = np.array( [i for i in range(10, 31) if i % 10 == 0 ])
print(a, b) # [1 2 3] [10 20 30]

print(a * 2 + b) # [12 24 36]
print(np.exp(a))    # [  2.71828183   7.3890561   20.08553692]
print(np.log(b))    # [ 2.30258509  2.99573227  3.40119738]
print(np.sin(a))    # [ 0.84147098  0.90929743  0.14112001]


""" 
 3. 2차원 배열 만들기
 
 ndarray : N-dimensional Array의 약자
"""
print("=" * 50)
print("3. 2차원 배열 만들기")
print("=" * 50)


a = np.array( [[1, 2, 3], [4, 5, 6]] )
print(a) # 2행 3열 array
print(a.shape)  # (2, 3) : 2행 3열
print(len(a))   # 2
print(len(a[0]))    # 3
print(a.ndim)  # 2차원

# 1행 2열의 데이터를 확인하고 싶다면?
print(a[0, 1])  # 2

"""
연습 문제 1

다음과 같은 행렬을 만든다.

10 20 30 40
50 60 70 80
"""
a = np.arange(10, 90, 10).reshape(2, 4)
print(a)

b = np.array( [[10, 20, 30, 40], [50, 60, 70, 80]] )
print(b)

"""
 4. 3차원 배열 만들기
"""
print("=" * 50)
print("4. 3차원 배열 만들기")
print("=" * 50)


a = np.array( [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]] )
print(a)
print(a.shape) # 2면 3행 4열
print(len(a))   # 2
print(len(a[0])) # 3
print(len(a[0][0])) # 4

# a[면, 행, 열]
# 2면의 2행 3열의 데이터를 확인하고 싶다면?
print(a[1, 1, 2]) # 19

# 1면의 3행 3열의 데이터를 확인하고 싶다면?
print(a[0, 2, 2]) # 11


"""
5. 배열의 차원과 크기 알아내기

ndim, shape
"""
print("=" * 50)
print("5. 배열의 차원과 크기 알아내기")
print("=" * 50)


print(a)
print(a.ndim)   # 3 : 3차원
print(a.shape)  # (2, 3, 4)

"""
 6. 배열의 indexing
 
 7. 배열의 slicing
"""
print("=" * 50)
print("6. 배열의 indexing")
print("7. 배열의 slicing")
print("=" * 50)


print(a)
# [[[ 1  2  3  4]
#   [ 5  6  7  8]
#   [ 9 10 11 12]]
#
#  [[13 14 15 16]
#   [17 18 19 20]
#   [21 22 23 24]]]

print("shape:", a.shape) # 2면, 3행, 4열
print("ndim:", a.ndim) # 3차원

# 마지막 면의 마지막행, 마지막 열 값
print(a[-1, -1, -1]) # 24

#  1면, 1행, 1열 값
print(a[0, 0, 0])  # 1

# 2면, 3행, 2열 값
print(a[1, 2, 1]) # 22

# 1면 1행 전체
print(a[0, 0])   # [1 2 3 4]

# 2면 2열 전체
print(a[1, :, 1])   # [14 18 22]

# 2면 두번째 행의 두번째 열부터 열 끝까지
print(a[1, 1:, 1:])

# 1면에 2번째 행 3번째 열까지만 출력
print(a[0, :2, :3])

"""
연습 문제 2

다음 행렬과 같은 행렬이 있다.

m = array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
이 행렬에서 값 7 을 인덱싱한다.
이 행렬에서 값 14 을 인덱싱한다.
이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다.
"""

m = np.arange(0, 15).reshape(3, 5)
print(m)
print("ndim:", m.ndim)  # 2차원
print("shape:", m.shape) # 3행 5열

# value 7 indexing
print(m[1, 2])

# value 14 indexing
print(m[-1, -1])

# value 6, 7 slicing
print(m[1, 1:3])

# value 7, 12 slicing
print(m[1:3, 2])

# value [3, 4], [8, 9] slicing
a = [list(m[0, 3:5]), list(m[1, 3:5])]
print(a)    # [[3, 4], [8, 9]]
print(np.array(a))
b = m[0:2, 3:5]
print(b)


"""
 8. fancy indexing( array indexing )
 
 배열 인덱싱에서는 대괄호(Bracket, [])안의 인덱스 정보로 숫자나 슬라이스가 아니라
 위치 정보를 나타내는 또 다른 ndarray 배열을 받을 수 있다.
 여기에서는 이 배열을 편의상 인덱스 배열이라고 부르겠다.
 
 배열 인덱싱의 방식
 1. 불리안(Boolean) 배열 방식
 2.정수 배열 방식 
"""
print("=" * 50)
print("8. fancy indexing( array indexing )")
print("=" * 50)

# 1. boolean 배열 방식
a = np.arange(0, 10)
print(a)

idx = np.array([True, False, True, False, True, False, True, False, True, False])
print(idx)
print(a[idx])   # [0 2 4 6 8]

# 조건문 연산 사용
print(a[a % 2 == 0])

# 2. 정수 배열 방식
print(a)
idx = np.arange(0, 10, 2)
print(idx)
print(a[idx])   # [0 2 4 6 8]

a = a * 10
print(a)   # [ 0 10 20 30 40 50 60 70 80 90]
print(a[idx])   # [ 0 20 40 60 80]

# array index size는 원래의 array size와 달라도 상관없음
l = [0, 1, 2]
idx = np.array([sorted(l * 5)]) # [[0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]]
print(idx)
print(a[idx])   # [[ 0  0  0  0  0 10 10 10 10 10 20 20 20 20 20]]


# 다차원 배열에도 사용 가능
print("=" * 50)
a = np.arange(1, 13).reshape(3, 4)
print(a)

# 1열과 4열만 보고 싶을 경우
print(a[:, [True, False, False, True]])

# 순서를 3행 1행 2행으로 변경
print(a[[2, 0, 1], :])

