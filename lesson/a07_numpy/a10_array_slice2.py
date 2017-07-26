'''
Created on 2017-07-26 09:56

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 array에서 데이터 조건에 합당한 내용 처리하기
 
 1. 형식
    배열[ 조건-boolean ]
    
    1) boolean 값 : ==, !=, ~(==), & (and), | (or)
    
        ex) a[ b = "A" ] : b array에 A인 경우에는 True 그렇지 않으면 False
            해당 array의 값이 True인 경우(행/열) 인 할당(slice) 처리
    
    
    2) boolean값, index
       boolean값이 true인 경우, 해당 행 또는 열의 index 두가지 조건을 다 만족하는 경우
       
       ex) a[b == "A", 2] : "A"인 경우 행/열인 경우와 index가 열/행 경우만 slicing
        
        
    3) boolean값, index시작:index마지막
        
        ex) a[b == "A", 0:2] : 열의 0 ~ 2까지
"""

import numpy as np

# 0~19, 5행 4열
a = np.arange(20).reshape(5, 4)
# 1차원 길이 5 array
b = np.array(["A", "B", "C", "A", "C"])

print(a)
print(b)

# b의 element값이 A인지 여부를 boolean값 처리
print(b == "A") # [ True False False  True False]

c = b == "A"

print(c)

## a array에 [ ] 안에 위에 있는 c를 입력하면

print(a[c]) # 1행, 4행만 나옴(동일한 해당 배열의 값 중 True값만 출력)

# a[행조건, 열index]
print(a[b == "A", 2]) # 1행, 4행의 3번째 열 element 확인
print(a[b == "A", :2]) # 1행, 4행의 1~2번째 열까지의 element 확인


"""
 ex)
 학생 5명의 과목별(3) 점수를 처리하고자 한다.
 해당하는 배열을 만들고, 과목명을 문자열로 배열을 만들어
 1) 첫번째 과목의 점수를 리턴
 2) 세번째 과목의 점수를 리턴
 3) 80점 이상인 과목의 점수를 리턴
 4) 두번째 과목의 2번쨰 학생의 점수를 리턴
"""

score = np.random.randint(0, 100, 15).reshape(5, 3)
print("==학생별 성적표==")
print(score)
subject = np.array(["kor", "math", "eng"])

# 1. 첫번째 과목(kor)
print("==국어 성적표==")
print(score[:, subject == "kor"])

# 2. 세번째 과목(eng)
print("==영어 성적표==")
print(score[:, subject == "eng"])

# 3. 점수가 80점 이상인 과목의 점수를 리턴
print("==80점 이상인 점수==")
print(score[score >= 80])

# 4. 두번째 과목의 2번째 학생의 점수를 리턴
print("==두번째 과목의 두번째 학생 점수=")
print(score[1, subject == "math"])