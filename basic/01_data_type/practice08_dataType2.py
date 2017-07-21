"""
 data type's true and false

 값	             참 or 거짓
 "python"	        참
 ""	               거짓
 [1, 2, 3]	        참
 []	               거짓
 ()	               거짓
 {}	               거짓
 1	                참
 0	               거짓
 None	           거짓

 """
from copy import copy

"""
  1. how to use true and false ?
"""
print("=" * 50)
print("1. how to use true and false ?")
print("=" * 50)
ex = [1, 2, 3, 4]
print(ex)

while ex:
    print(ex.pop())
# 4
# 3
# 2
# 1

# [] 은 false이다. false가 될 때까지 ex list에서 data를 끄집어내는 logic

if []:
    print(True)
else:
    print(False)
# [] 는 false이기 때문에 False가 출력된다.

ex = [1, 2, 3, 4]
if ex:
    print(True)
else:
    print(False)
# list에 data가 존재하기 때문에 True가 출력

"""
 2. 변수 : 자료형의 값을 저장하는 공간
 a = 3
 a를 변수라고 한다.
 변수명 = 변수에 저장할 값
 3이라는 값을 가지는 정수 자료형(객체)이 자동으로 메모리에 생성.
 a는 변수 이름이며, 3이라는 정수형 객체가 저장된 메모리 위치를 가리키게 된다.
 
"""
a = 3
b = 3
# 3은 상수가 아닌 정수형 객체이다.
print(type(3))  # <class 'int'>
print(a is 3)   # True
print(a is b)   # True

# 3이라는 객체를 가리키고 있는 변수의 개수는 2개이다. (Reference Count : 2)
# c = 3이라고 입력한다면 Reference Count : 3
c = 3

# a, b, c는 같은 객체를 가리키는 것인가?
# sys.getrefcount() : 참조 개수를 알려주는 함수
import sys
print(sys.getrefcount(3))   # 50 python 내부적으로 사용했기에 3이 아니다.
# 3을 가리키는 변수를 늘리면?
d = 3
print(sys.getrefcount(3))   # 51
e = 3
print(sys.getrefcount(3))   # 52
# 변수를 추가할 때 마다 sys.getrefcount 수가 1씩 증가한다.


"""
 변수를 만드는 여러가지 방법
"""
# 1.
a, b = ("ronaldo", "messi")
print(a, b)     # ronaldo messi
# 2.
a, b = "a", "b"
print(a, b)     # a b
# 3.
(a, b) = 1, 2
print(a, b)     # 1 2
# 4. list도 가능
[a, b] = ["name", "age"]
print(a, b)     # name age
# 5.
a = b = "king"
print(a, b)     # king king

# 6. 변수값 서로 바꾸기
a = "yoda"
b = "starwarz"
print(a, b)     # yoda starwarz
a, b = b, a
print(a, b)     # starwarz yoda

"""
 메모리에 생성된 변수 없애기
"""
a = 3
print(a)    # 3
del(a)
# print(a) NameError: name 'a' is not defined

"""
 리스트를 변수에 넣고 복사하고자 할 때
"""
a = [1, 2, 3]
print(a)    # [1, 2, 3]
b = a
print(b)    # [1, 2, 3]
a[1] = 4
print(a)    # [1, 4, 3]
print(b)    # [1, 4, 3]
# a의 index 첫번째 값을 바꿨는데 b의 index 첫번째 값도 바뀜
# a = b를 선언해서 변수명만 다를 뿐이지 동일한 list를 가리키고 있기 때문
print( b is a)   # True


"""
 그렇다면 같은 값을 복사하면서 서로 다른 list를 가리키는 방법은 없는가?
"""
# 1. [:] 이용
a = [1, 2, 3]
b = a[:]
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3]
print(b is a)   # False
a[1] = 4
print(a)    # [1, 4, 3]
print(b)    # [1, 2, 3]

# 2. copy module1 이용 : from copy import copy 선언

a = [1, 2, 3]
b = copy(a)
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3]
print(b is a)   # False

# 같은 값이지만 서로 다른 객체이다.
