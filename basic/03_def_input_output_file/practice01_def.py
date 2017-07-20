"""
 def ( function )

 def 함수명(parameter):
    문장1
    문장2
    [return 리턴값]
 paramter = 매개변수, 입력 인수
"""


# ex1. 전달받은 2개의 수를 더하여 결과값(return)으로 돌려주기
def sumDef(a, b):
    x = a + b
    return x


print(sumDef(3, 4))  # 7

c = 7
d = 12
result = sumDef(c, d)
print(c, d, result)  # 7 12 19

"""
 parameter값이 없는 def
"""


def say1():
    print("hi")


say1()  # hi


def say2():
    return "hello"


print(say2())  # hello
a = say2()
print(a)  # hello

"""
 return 값이 없는 def
"""


def sum(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


a = sum(3, 4)  # 3, 4의 합은 7입니다.
print(a)  # return 값이 없기 때문에 None으로 나옴

"""
 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
 
 def 함수이름(*입력변수): 
    <수행할 문장>
    ...
    
"""


# 입력값을 모두 더하는 함수 만들기(입력값의 갯수를 사전에 정해놓지 않음)
def sum_what(*args):
    result = ""
    for i in args:
        result += i
    return result


print(sum_what("a", "b", "c"))  # abc
print(sum_what("r", "o", "n", "a", "l", 'd', "o"))  # ronaldo


# parameter 값으로 def logic 선택
def process(choice, *args):
    if choice == "plus":
        result = 0
        for i in args:
            result += i
    elif choice == "minus":
        result = 0
        for i in args:
            result -= i
    elif choice == "multi":
        result = 1
        for i in args:
            result *= i
    return result


print(process("plus", 1, 2, 3, 4, 5))  # 15
print(process("minus", 1, 2, 3, 4, 5))  # -15
print(process("multi", 1, 2, 3, 4, 5))  # 120

"""
 함수의 결과값은 언제나 하나이다
"""


def sum_mul(a, b):
    return a + b, a * b


result = sum_mul(3, 4)
print(result)  # (7, 12) tuple로 나옴 (a+b, a*b)

"""
 return 값을 2개 이상 쓸 수 없다.
 def f1(a, b):
    return a+b   ----> 첫번째 return 값만 돌려주고 해당 def를 탈출하게 되서
    return a*b   ----> 두번째 return 값은 실행이 되지 않는다.
    
 따라서 return은 해당 함수를 탈출하고자 할 경우에도 많이 사용된다.
"""


def say_name(nick):
    if nick == "yoda":
        return
    print("my nickname is %s." % nick)


say_name("ronaldo")  # my nickname is ronaldo.
say_name("yoda")  # print 실행하지 않고 바로 탈출

"""
 입력 인수에 초기값 미리 설정하기
"""


def intro(name, age, gender=True):
    print("my name is %s" % name)
    print("I'm %i old" % age)
    if gender:
        print("gender: man")
    else:
        print("gender: woman")


intro("ronaldo", 32)
intro("messi", 37, True)
intro("keeley hazel", 25, False)  # gender : woman 으로 나옴

"""
 def 안에서 선언된 변수의 효력 범위
"""

a = 1
def test(a):
    a = 3

test(a)
print(a)  # 1 : 함수를 적용하고 print 했음에도 4가 아닌 1로 나옴

def test2(a):
    a = a + 3
    return a

test2(a)
print(a)    # 1

"""
 함수 안에서 함수 밖의 변수를 변경하는 방법
"""

# 1. return 값을 이용하여 변수 재 선언
a = test2(a)    # a변수를 def결과로 다시 선언
print(a)    # 4

# 2. global 명령어 이용하기
a = 1
print(a)  # 1
def test3():
    global a
    a = a+10

test3()
print(a) # 11 로 변경

b = 3
def test4():
    global new
    new = 15

test4()
print(new)  # 함수에서 선언한 변수 new가 함수 밖에서도 사용 가능
# 그러나 가급적 첫번째 방법을 이용
