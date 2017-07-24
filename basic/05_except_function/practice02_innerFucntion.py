'''
Created on 2017-07-24 11:29

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 1. abs(x) : 절대값
"""
print("=" * 50)
print("1. abs() ")
print("=" * 50)

x = - 3.415
print(x)
print(abs(x))

"""
 2. all(x) : x가 모두 true면 True, false가 하나라도 있으면 False return
  
 x : 반복 가능한(iterable) 자료형
     ex) list, tuple, dict, set
"""
print("=" * 50)
print("2. all(x)")
print("=" * 50)

x = [1, 2, 3]
print(all(x))   # True

x = 1, 2, 3, 0
print(all(x))   # False : 0은 False 처리

x = True, False, True
print(all(x))

"""
 3. any(x) : all(x)의 반대. 하나라도 참이 있을 경우 True, 모두 False일 경우에만 False return.
"""
print("=" * 50)
print("3. any(x)")
print("=" * 50)

x = [1, 2, False, 3, 4, 0]
print(any(x))   # True

x = [0, ""]
print(any(x))   # False

"""
 4. chr() : 아스키(ASCII) code를 입력으로 받아 그 code에 해당하는 문자 출력
"""
print("=" * 50)
print("4. chr() ")
print("=" * 50)

print(chr(97))  # a

for i in range(1, 101):
    print(chr(i))



"""
 5. dir() : 객체가 자체적으로 가지고 있느 변수나 함수를 보여 줌
"""
print("=" * 50)
print("5. dir()")
print("=" * 50)

print(dir([1, 2, 3])) # lsit가 가지고 있는 method
print(dir({"1": "a"})) # dict가 가지고 있는 method



"""
 6. divmod(a, b) : a를 b로 나눈 몫과 나머지를 tuple형태로 반환
"""
print("=" * 50)
print("6. divmod(a, b)")
print("=" * 50)

print(divmod(10, 2)) # 5, 0
print(divmod(15, 7)) # 2, 1


"""
 7. enumerate() : 열거하다. 자료형을 입려긍로 받아 인덱스를 포함하는 enumerate 객체를 return
"""
print("=" * 50)
a = {"name": "ronaldo", "age": 25, "loc": "portugal", "rival": "messi"}

for i, name in enumerate(a):
    print(i, name)
# 0 name
# 1 age
# 2 loc
# 3 rival

b = ("a", "b", "c", "d", "e")
for i, name in enumerate(b):
    print(i, name)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

"""
 8, eval : 수식이 포함된 문자열을 가능하게 해줌
"""
print("=" * 50)

str = "1+2+34+12.551"
print(eval(str))    # 49.551
str = "'hi' + 'man'"
print(eval(str))    # himan


"""
 9. filter(def, x) : def(함수이름), x(자료형 data)
"""
print("=" * 50)

def positive(x):
    result = []
    for i in x:
        if i > 0:
            result.append(i)
    return result

a = [1, 2, 3, -34, -32.1, 0, 3.213, 1]
print(positive(a))


def positive(x):
    return x > 0

print(list(filter(positive, a)))

print( list( filter(lambda x: x > 0, a) ) )

"""
 10. hex() : 정수값을 입력받아 16진수(hexadecimal)로 return
"""
print("=" * 50)

print(hex(10))
print(hex(-12))
print(hex(124523))

"""
 11. id(object) : 객체를 입력받아 객체의 고유 주소값(reference)를 return
"""
print("=" * 50)

a = 3
b = 3
c = a
print(id(a))
print(id(b))
print(id(c))

import copy
d = copy.copy(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))

# id값 동일


"""
 12. input() : 사용자 입력을 받는 함수
"""
# print("=" * 50)
#
# a = input()
# print(a)
#
# b = input("Enter: ")
# print(b)


"""
 13. int : 문자열 형태의 숫자나 float 숫자를 정수형태로 return
"""
print("=" * 50)

a = ["1", 12.34, -12.11, "-13455"]
print(a)
for i in a:
    print(int(i))
# 1
# 12
# -12
# -13455

# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 return

print( int("11", 2) )   # 2진수로 표현된 '11'의 10진수 값 : 3
print( int("10A", 16) ) # 16진수로 표현된 '10A'의 10진수 값 : 266


"""
 14. isinstance(object, class) : 객체(object)가 class의 instance인지 확인.
"""
print("=" * 50)

class Person: pass

a = Person()
print(isinstance(a, Person))    # True

"""
 15. lambda : 함수를 생성할 때 사용하는 예약어. def와 동일한 역활.
 
 lambda 인수1, 인수2, ... : 인수를 이용한 표현식
"""
print("=" * 50)

result1 = lambda a, b: a + b

print(result1(3, 5)) # 8

def result2(a, b):
    result = a + b
    return result

print(result2(15, 3))   # 18


mylist = [lambda a, b: a + b, lambda a, b: a * b]
print(mylist)
# [<function <lambda> at 0x00000000028FE488>, <function <lambda> at 0x00000000028FE510>]
print(mylist[0](3, 5))
print(mylist[1](3, 5))

"""
 16. len(x) : x의 길이(element의 전체 개수) return
"""
print("=" * 50)

print(len(mylist)) # 2
print(len([1, 2, 3]))   # 3
print(len("asdadsadada"))   # 11


"""
 17. list(x) : list로 casting
"""
print("=" * 50)
print(list("HELLO"))  # ['H', 'E', 'L', 'L', 'O']
a = [1, 2, 3]
b = a
c = copy.copy(a)
d = a[0:]
print(id(a))
print(id(b))
print(id(c))
print(id(d))

# a, b는 주소값이 같으나 c, d는 다름

"""
 18. map(def, x) : 함수(def)와 반복 가능한(iterable) 자료형(x)을 입력으로 받는다.
"""
print("=" * 50)

def double(x):
    result = []
    for i in x:
        result.append(i * 2)
    return result

a = [1, 2, 3]
print(double(a))

def double(x):
    return x * 2

b = map(double, a)
print(list(b))

# [2, 4, 6]

c = map(lambda x: x * 2, a)
print(list(c))

# [2, 4, 6]


"""
 19. max(x) : 최대값을 return ( 문자형도 가능 )
"""
print("=" * 50)

print(max(1, 2, 3, 4))
print(max("asafaaz"))   # z
print(max("가나다드그")) # 한글도 가능
# max 한글 > 영어 > 숫자

"""
 20. oct(x) : 8진수 문자열로 return
"""
print("=" * 50)

print(oct(34))  # 0o42


"""
 21. open(filename, [mode]) : 파일 객체 return
 mode	        설명
 w	            쓰기 모드로 파일 열기
 r	            읽기 모드로 파일 열기
 a	            추가 모드로 파일 열기
 b	            바이너리 모드로 파일 열기
 
 b는 w, r, a와 함께 사용
 
"""
print("=" * 50)

f = open("foo.txt", "rb")
a = f.read()
print(a)

f1 = open("foo.txt", "a")
f1.write("aaaaaa") # 쓰기
f1.close()


"""
 22. ord(x) : 문자의 아스키 코드값을 리턴
"""
print("=" * 50)

print(ord("a")) # 97
print(chr(97))  # a

"""
 23. pow(x, y) : x의 y제곱
"""
print("=" * 50)
print( pow(2, 4) )  # 16
print( pow(4, -2) ) # 0.0625

"""
 24.range([start,] stop [,step])
"""
print("=" * 50)

# 1. 인수가 하나인 경우
print( list(range(10)) ) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 인수가 두개인 경우
print( list(range(1, 10)) ) # [1, 2, 3, 4, 5, 6, 7, 8, 9] 1<= x < 10

# 3. 인수가 3개인 경우
print( list(range(1, 10, 2)) )  # [1, 3, 5, 7, 9]


"""
 25. sorted(x) : x를 순서대로 정렬
"""
print("=" * 50)

a = [5, 4, 12, 1, 4, 7, 2]
print( sorted(a) )  # [1, 2, 4, 4, 5, 7, 12]
print( sorted(a, reverse=True) )    # [12, 7, 5, 4, 4, 2, 1] 역순
a = "addaswdas"


"""
 26. zip(x) : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
"""

print("=" * 50)
a = [1, 2, 3]
b = ["a", "b", "c"]
c1 = zip(a, b)
c2 = zip(a, b)
c3 = zip(a, b)
print(list(c1))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(c2))  # ((1, 'a'), (2, 'b'), (3, 'c'))
print(dict(c3))  # {1: 'a', 2: 'b', 3: 'c'}