'''
Created on 2017-07-25 14:57

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 ndarray의 산술 연산
 
 1. 배열과 숫자 데이터 연산은 배열의 각 elements의 연산 결과를 return

 2. 동일 크기를 갖는 배열은 동일한 위치의 element끼리 연산 수행
 
     ex)
        a = np.arange(1, 4)
        b = np.arange(3, 6)
        c = a * 2  : a의 각 element마다 *2를 처리하여 return 
        c = [2, 4, 6]
        d = a + b : a의 element와 b의 element를 더하여 return
        d = [4, 6, 8]
        
 
 3 . 비교 연산도 동일한 위치의 element를 비교
    np.not_equal(a, b), np.equal(a, b), np.greater(a, b), np.greater_equal(a, b)
    np.less(a, b), np.less_equal(a, b)
    ex) 
        b = np.equal(a, b)
        b = [False, False, False]
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 2, 6])
c = np.array( [[6, 7, 3], [10, 20, 30]])

# array 연산
print(a * 2)
print(a + b)
print(a * b)
print(a * c)
print(b + c)

# array 간 비교 연산
# 왼쪽이 오른쪽이랑 같은지, 또는 왼쪽이 오른쪽보다 크거나 같은지 (기준은 왼쪽부터)
# 동등한지
print("-" * 50)
print(np.equal(a, b))
print(np.equal(a, c))
print("-" * 50)
print(np.greater(a, b))
print(np.greater(c, b))
print("-" * 50)
print(np.greater_equal(a, b))
print(np.greater_equal(c, a))
print("-" * 50)
print(np.not_equal(a, b))
print("-" * 50)
print(np.less(a, b))
print("-" * 50)
print(np.less_equal(c, b))
print(np.less_equal(b, c))


"""
 ex) 
 subject : java, jsp, spring
 3명으로 점수 할당 처리
 1. 평균점수 70점 이상일시 pass 처리
 2. 각 과목별로 pass 여부 출력
"""

java = np.random.randint(35, 100, 3)
jsp = np.random.randint(35, 100, 3)
spring = np.random.randint(35, 100, 3)

score = [java, jsp, spring]
score = np.array(score)


# 1. 과목별로 pass 여부 출력
isPass = 70
print('''
=== 과목별 점수 ===
1. java
2. jsp
3. spring
''')
print(score)
print("===커트라인===")
print(isPass)
print(np.greater_equal(score, isPass))

# 2. 평균점수로 pass여부 출력
avg = []
for i in score:
    avg.append(sum(i)/3)

print('''
=== 과목별 평균점수 ===
1. java
2. jsp
3. spring
''')
print(avg)
print("===커트라인===")
print(isPass)
print(np.greater_equal(avg, isPass))

print("-" * 50)

a = np.array([10, 20, 30])
b = np.arange(12).reshape(4, 3)
print(a)
print(b)

# a 배열과 b 배열의 같은 열에 위치한 element 연산
print(a + b)

a = np.linspace(10, 30, 3).reshape(3, 1)
b = np.arange(12).reshape(3, 4)
print(a) # 3행 1열
print(b) # 3행 4열

# a배열과 b 배열의 같은 행에 위치한 element 연산
print(a + b)
