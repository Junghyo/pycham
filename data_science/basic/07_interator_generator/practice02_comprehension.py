'''
Created on 2017-07-24 19:52

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 list comprehension
 
 입력 Sequence로부터 지정된 표현식에 따라 새로운 리스트 컬렉션을 빌드하는 것으로,
 아래와 같은 문법을 갖는다.
 
 [출력표현식 for 요소 in 입력Sequence [if 조건식]]
"""

old = [1, 2, 'A', 13, "13", False]

new = [x for x in old if type(x) == int]
# old list에서 숫자만 가지고 new list 만들기
print(new)  # [1, 2, 13]


"""
 set comprehension
 
 {출력표현식 for 요소 in 입력Sequence [if 조건식]}
 
"""

old = [1, 2, 3, 5, 1, 3, 5, 22, 1, 17]
# old list에서 같은 값을 곱하여 새로운 list 만들기
new = {x * x for x in old}
print(new)

new1 = [x * x for x in old]
print(new1)
print(set(new1))

# 중복된 숫자는 하나만 표시되며 순서는 random

"""
 dict comprehension
 {Key:Value for 요소 in 입력Sequence [if 조건식]}
"""

id_name = {1: "lee", 2: "kim", 3: "seo"}

name_id = {value: key for key, value in id_name.items()}
print(name_id)  # {'lee': 1, 'kim': 2, 'seo': 3}

def isodd(x):
    return x % 2 == 1

# 1부터 100까지 홀수를 Dictionary Key로 하고, 그 홀수의 제곱을 Value로 하는 dict 객체를 생성한다.
mydict = {(str(x)+"key"): (str(x * x)+"value") for x in range(101) if isodd(x)}
print(mydict) # {'1key': '1value', '3key': '9value',.....