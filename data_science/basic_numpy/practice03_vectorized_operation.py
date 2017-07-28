'''
Created on 2017-07-25 18:08

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 vectorlized operation
 
"""
import numpy as np

# 만약 벡터화 연산을 사용하지 않는다면?
x = np.arange(1, 1001)
y = np.arange(1001, 2001)
z = np.zeros_like(x)

for i in range(1000):
    z[i] = x[i] + y[i]

print(z[:10])

# 하지만 벡터화 연산을 사용한다면
z1 = x + y
print(z1[:10])


# 비교도 가능하다

a = np.array([1, 3, 3, 4, 7])
b = np.arange(1, 6)
c = np.arange(1, 6)
print(a == b)    #[ True False  True  True False]

print(a >= b)

# 만약 배열 전체를 비교하고 싶다면 all을 사용한다
print(np.all(b == c)) # True
print(np.all(a > b))  # False

# 지수 함수, 로그 함수 등의 수학 함수도 벡터화 연산을 지원한다.
a = np.arange(5)
print(np.exp(a)) # 지수 함수
# print(np.log(a)) # 로그 함수
print(10 ** a)
# print(np.log10(a))

print(np.log10(10))  # 1

"""
연습 문제 1

벡터 x가 다음과 같을 때, 여러가지 수식을 사용하여 같은 크기의 벡터 y를 만든다.

x = np.arange(10)
"""
x = np.arange(10)
y = x
print(y)
z = np.linspace(1, 10, 10)
print(z)
x1 = np.array([i for i in range(10)])
print(x1)


"""
 scala와 vector/array의 곱셈
 
 스칼라와 벡터/행렬의 곱도 선형 대수에서 사용하는 식과 NumPy 코드가 일치한다.
"""
print("=" * 50)

x = np.arange(10)

print(x * 100)

x = np.arange(12).reshape(3, 4)

print(100 * x)


"""
 broadcasting
 
 크기가 작은 배열을 자동으로 반복 확장하여 크기가 큰 배열에 맞추는 방법(numpy 지원)
 
 ex)
 선형대수에서
 x = np.range(5); y = 1
 x + y 불가
 vector + scala는 연산이 불가능
 
 하지만 numpy는 y를 자동적으로 x vector의 크기만큼 확장시켜서 계산이 가능

"""
print("=" * 50)

x = np.arange(5)
y = np.ones_like(x)

print(x)
print(y)
print(x + y)    # [1 2 3 4 5]

y = 1

print(x + y)    # [1 2 3 4 5]

# 차원이 높은 경우
print("=" * 50)


a = np.arange(0, 31, 10)
print(a)    # [ 0 10 20 30]

a1 = np.tile(a, (3, 1)) # a array를 행으로 3번 복사 열로는 1번 복사
print(a1)

a = a1.T # 전치행렬. 행과 열을 바꿈
print(a)

b = np.arange(3)
print(b)

print(a + b)

print("=" * 50)


a = np.arange(0, 40, 10)
print(a)
print("ndim:", a.ndim) # 1
print("shape:", a.shape) # (4, )

a = a[:, np.newaxis] # 1차원 증가
print(a)
# [[ 0]
#  [10]
#  [20]
#  [30]]
print("ndim:", a.ndim) # 2
print("shape:", a.shape) # (4, 1)

print(b + a)
print(a + b)
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]

# 자동으로 각 array들의 행, 열 크기에 맞춰 늘어나서 연산됨

"""
 dimension reduction operation
 
 행렬의 하나의 행에 있는 원소들을 하나의 데이터 집합으로 보고
 그 집합의 평균을 구하면 각 행에 대해 하나의 숫자가 나오게 된다.
 예를 들어 10x5 크기의 2차원 배열에 대해 행-평균을 구하면
 10개의 숫자를 가진 1차원 벡터가 나오게 된다.
 이러한 연산을 차원 축소(dimension reduction) 연산이라고 한다
"""
print("=" * 50)

a = np.random.random_integers(0, 100, 50).reshape(10, 5)
print(a)
print(np.mean(a, axis=1, keepdims=True))
print(a.mean())
# 전체를 1차원이라 생각했을 때 가장 작은 값의 index 위치
print(a.argmin())
# 각 행 마다 가장 작은 값의 위치
print(a.argmin(axis=1))
# 각 열 마다 가장 작은 값의 위치
print(a.argmin(axis=0))

x = np.array([1, 2, 3, 5, 0])
print(np.sum(x))
print(x.sum())
print(np.min(x))
print(x.max())
print(x.argmin()) # 최소값의 index 위치
print(x.mean()) # 평균
print(np.median(x)) # 중앙값
# all  하나라도 false(=0) 값이 있으면 False
print(np.all(x))
# any 하나라도 true 값이 있으면 True
print(np.any(x))

# 0값으로 100행 100열 만들기. datatype = int
a = np.zeros((100, 100), dtype=np.int)
print(a)

# 각 element 마다 조건 비교
print(a != 0)
# 전체 중 하나라도 0이 아니면 True
print(np.any( a != 0))
# 전체 중 하나라도 0이면 True
print(np.any(a == 0))
# 전체가 모두 0이면 True
print(np.all(a == 0))
# a가 a면 True
print(np.all(a == a))

print("=" * 50)

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])

# a >= b 그리고 b <= c 중 둘 중 하나라도 맞으면 True
print(((a >= b) & (b <= c)).any())
# a >= b 그리고 b <= c 전부 맞으면 True
print(((a >= b) & (b <= c)).all())

"""
 연산의 대상이 2차원인 경우 어느 차우너으로 계산 할 지를 axis로 명시.
 axis = 0 : 열
 axis = 1 : 행
"""
print("=" * 50)

x = np.arange(1, 5).reshape(2, 2)
print(x)
# 전체 합계
print(np.sum(x))
print(x.sum())

# 곱셈
print(x.prod()) # 전체 곱셈
print(x.prod(axis=0)) # 열 곱셈
print(x.prod(axis=1)) # 행 곱셈

# 나누기
print(np.divide(x, 2)) # 각 element를 2로 나눈 값을 return

# 나머지 반환
print(np.mod(x, 2)) # 각 element를 2로 나눈 나머지값을 return

# root
print(np.sqrt(x))

# square
print(np.square(x)) # 제곱

"""
연습 문제 2

5 x 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.

전체의 최댓값
각 행의 합
각 열의 평균
"""

a = np.arange(1, 31).reshape(5, 6)
print(a)

# 전체의 최댓값
print(np.max(a)) # 30
# 각 행의 합
print(np.sum(a, axis=1, keepdims=True))
# 각 열의 평균
print(np.mean(a, axis=0, keepdims=True))


"""
 sort
"""

a = np.array([[4, 3, 12], [12, 2, 7]])
print("=" * 50)
print(a)
a.sort(axis=0) # 열단위로 정렬
print(a)
a.sort(axis=1) # 행단위로 정렬
print(a)


# 정렬이 아닌 순서만 알고 싶다면 argsort()사용
a = np.random.random_integers(1, 15, 4)
print(a)
idx = a.argsort()
print(a[idx])

"""
연습 문제 3

다음 배열은 첫번째 행(row)에 학번, 두번째 행에 영어 성적,
세번째 행에 수학 성적을 적은 배열이다. 영어 성적을 기준으로 각 열(column)을 재정렬하라.

array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])
"""
print("=" * 50)

info = np.array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])

print(info)

# 영어 성적 순으로 정렬
print(info[:, info[1].argsort()])
