'''
Created on 2017-07-21 09:55

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 Python : 객체지향 프로그래밍(Object Oriented Programming)
 
 class : 설계 도면. 뽑키틀
 
 class's member :  메서드(method), 속성(property), 클래스 변수(class variable), 인스턴스 변수(instance variable), 
                   초기자(initializer), 소멸자(destructor)
                   
"""
# def 사용
# 2개의 계산기가 필요할 경우 함수를 각각 2개를 만들어야함
result1 = 0
result2 = 0
def adder1(num):
    global result1
    result1 += num
    return result1

print(adder1(1))
print(adder1(2))
print(adder1(5))


def adder2(num):
    global result2
    result2 += num
    return result2

print(adder2(1))
print(adder2(5))
print(adder2(7))

# class 사용
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):   # def를 한번만 정의
        self.result += num
        return self.result

# 각각의 변수에 class 선언
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

"""
 객체 (Object) : class에 의해 만들어짐.
 
 1개의 class는 무수히 많은 Object를 만들 수 있다.
"""
# class basic ex
# 1. 클래스 생성
class Programmer:
    pass

# 2. Programmer class의 object를 만드는 법
yoda = Programmer()
ronaldo = Programmer()
# Programmer()의 결과값을 돌려받은 yoda와 ronaldo가 바로 object

"""
 객체와 인스턴스의 차이
 
 class에 의해서 만들어진 객체(object)를 인스턴스(instance)라고도 한다.
 kim = Programmer() 에서 kim은 object이다. 그리고 kim이라는 object는 Programmer의 instance이다.
 instance : 특정 object(ex: kim)가 어떤 class(Programmer)의 object인지 관계 위주로 설명할 때 사용.
 1. kim은 object
 2. kim은 class Programmer의 instance
"""

"""
 이야기 형식으로 class 기초 쌓기
"""

"""
 1. class variable
"""
print("=" * 50)
print("1. class variable")
print("=" * 50)

# class 생성. (service 업체라고 가정)
class Company:
    secret = "ronaldo is handsome" # class variable 선언
# 이 회사는 "ronaldo is handsome" 라는 비밀정보를 가지고 있다.

# 이 회사에 가입해보자.
yoda = Company()  # yoda라는 object 선언. yoda는 Company의 instance
# yoda라는 id로 Company에 가입

# yoda로 접속해서 비밀정보를 얻어보자
print(yoda.secret)  # ronaldo is handsome

"""
 해당 class의 instance인 object는 해당 class의 variable을 사용할 수 있다.
"""
# 회사에서 자신의 비밀정보 확인( Class명으로 variable 출력)
print(Company.secret)   # ronaldo is handsome

# 회사에서 비밀정보를 변경하고자 한다면?
Company.secret = "messi is short"

# yoda로 접속해서 비밀정보를 다시 확인해보자
print(yoda.secret)  # messi is short
# 정보가 update 된 것을 확인 가능

"""
 2. class method
"""
print("=" * 50)
print("2. class method")
print("=" * 50)

# Company에서 user들이 제공하는 숫자를 더해주는 service(def)를 제공하려고 한다.
class Company:
    secret = "messi is short" # class variable
    def plus(self, a, b):   # service(def) 선언
        result = a + b
        print("{0}+{1}={2}".format(a, b, result))

# 새로운 user가 가입한다.(object 생성)
kim = Company()

# Company의 service(def)를 이용해 본다.
kim.plus(3, 4)  # 3+4=7   parameter에 self도 있으나 이것은 object 자신으로 바로 할당됨.

# Company로 service를 이용해 본다.
# Company.plus(3, 5)  TypeError: plus() missing 1 required positional argument: 'b'
# error 발생. self parameter 값이 빠져 있기 때문 (class는 self가 될 수 없다)

Company.plus(kim, 3, 5) # 3+5=8  kim의 id(class's instance)를 무단으로 사용해서 이용할 수 있다.

# Company.plus(s, 3, 5) NameError: name 's' is not defined
# s라는 id(instance)가 없기 때문에 사용이 불가능 하다.



"""
 3. instance variable
 
 객체.객체변수 = 값
"""
print("=" * 50)
print("3. instance variable")
print("=" * 50)

# user들(해당 class의 instance)이 plus(def)를 이용할 때 자신의 이름이 나오도록 요구했다.
class Company:
    secret = "messi is short"
    def setname(self, name):   # instance variable
        self.name = name

    def plus(self, a, b):
        result = a + b
        print("Mr. %s, %i + %i = %i" % (self.name, a, b, result))

# 새로운 유저가 가입한다.
pey = Company()
pey.setname("messi") # pey라는 유저가 이름(instance variable)을 알려준다
print(pey.name) # messi. 이름이 입력이 잘 되었는지 확인
pey.plus(5, 6)  # Mr. messi, 5 + 6 = 11  이제 plus에서 해당 유저의 이름까지 알려준다.


"""
 4. initializer (초기자)
 __init__
 
 Java의 constructor(생성자)와 비슷한 개념이다.
"""
print("=" * 50)
print("4. initializer")
print("=" * 50)

# 새로운 user(instance)가 가입시 이름 설정을 깜빡하여 service(def)이용에 어려움을 겪고 있다고 한다.
id1 = Company()
# id1.plus(5, 4) AttributeError: 'Company' object has no attribute 'name'
# 이름을 설정하지 않아 service를 이용하지 못함.

# 그래서 __init__이라는 방법을 통해 회원가입시 바로 이름을 입력하도록 한다.
class Company:
    secret1 = "messi is short"
    secret2 = "ronaldo is great"
    count = 0   # instance 수 확인 위한 변수
    def __init__(self, name): # initializer 선언. object 생성시에 입력이 되도록
        self.name = name
        Company.count += 1  # instance 추가시 +1씩 증가
    def plus(self, a, b):
        result = a + b
        print("Mr. %s, %i + %i = %i" % (self.name, a, b, result))

# id1 = Company() TypeError: __init__() missing 1 required positional argument: 'name'
# 가입시 이름을 필수정보로 입력하도록 했기 때문에 이름을 적지 않으면 error 발생
id1 = Company("ronaldo")
print(id1.name) # ronaldo
id1.plus(10, 20)    # Mr. ronaldo, 10 + 20 = 30


# 한 학교에서 단체로 이 회사에 회원가입을 한다.
# for문으로 Company class의 object 생성
number = 0
for i in range(2, 20):
    id_i = Company("student"+str(i))
    print(id_i.name) # 각 object의 이름 출력
    number += 1
    id_i.plus(number, number*3)
    print("-" * 50)

# 회원수(instance)가 많아짐에 따라 얼마나 많은 사람이 회원가입을 했는지 알고 싶다.
# class variable로 count 설정
# initializer에 해당 object가 선언될 때마다 +1 씩 증가
print(Company.count)     # 총 19명의 user(instance)가 회원가입함


"""
 class 기본 구조
 
 class 클래스이름[(상속 클래스명)]:
    <클래스 변수 1>
    <클래스 변수 2>
    ...
    def 클래스함수1(self[, 인수1, 인수2,,,]):
        <수행할 문장 1>
        <수행할 문장 2>
        ...
    def 클래스함수2(self[, 인수1, 인수2,,,]):
        <수행할 문장1>
        <수행할 문장2>
        ...
    ...
"""
# 사칙연산 class 만들기(calculator)
print("=" * 50)
print("make calculator")
print("=" * 50)

# 1. class 만들기
class Calculator:
    pass

data = Calculator()
print(type(data))   # <class '__main__.Calculator'>

class Calculator:
    def setnum(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = "%i + %i = %i" % (self.num1, self.num2, self.num1 + self.num2)
        return result

    def minus(self):
        result = "%i - %i = %i" % (self.num1, self.num2, self.num1 - self.num2)
        return result

    def multi(self):
        result = "%i X %i = %i" % (self.num1, self.num2, self.num1 * self.num2)
        return result

    def div(self):
        result = "%i ÷ %i = %f" % (self.num1, self.num2, self.num1 / self.num2)
        return result

data = Calculator()
data.setnum(10, 2)
print(data.num1, data.num2) # 10, 2 제대로 숫자들이 들어간다.

Calculator.setnum(data, 15, 3) # class에서 직접 숫자 입력
print(data.num1, data.num2)  # 15, 3

print(data.plus())
print(data.minus())
print(data.multi())
print(data.div())

data2 = Calculator()
data2.setnum(17, 2)
print(data2.plus())
print(data2.minus())
print(data2.multi())
print(data2.div())

"""
 Lionel's House class 만들기
"""
print("=" * 50)
print("Lionel's House class")
print("=" * 50)

class HouseMessi:
    lastname = "Messi"

    def __init__(self, firstname):
        self.firstname = firstname
        self.fullname = firstname + " " + self.lastname

    def travel(self, where):
        print("%s is traveling %s" % (self.fullname, where))

person = HouseMessi("Lionel")
print(person.lastname)
print(person.firstname)
print(person.fullname)
person.travel("Seoul")


"""
 class's inheritance
"""
print("=" * 50)
print("class's inheritance")
print("=" * 50)

# make Jackson's House class
class HouseJackson(HouseMessi): # HouseMessi's class를 inheritance
    lastname="Jackson"

person1 = HouseJackson("Michael")
print(person1.lastname)
print(person1.firstname)
print(person1.fullname)
person1.travel("New York")


"""
 method overriding
 상속받은 class의 method를 다르게 동작하도록 만드는 것
"""
print("=" * 50)
print("method overriding")
print("=" * 50)

class HousePark(HouseJackson):
    lastname = "Park"

    def travel(self, where, friend):
        print("%s is traveling %s with %s" % (self.fullname, where, friend))

person2 = HousePark("Jisung")
print(person2.lastname)
print(person2.firstname)
print(person2.fullname)
person2.travel("Paris", "Yoda")

"""
 method overloading
"""
class HouseSmith(HousePark):
    lastname = "Smith"

    def love(self, other):
        print("%s is going out with %s" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s married %s" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s is fighting with %s" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s divorced %s" % (self.fullname, other.fullname))

person3 = HouseSmith("Sam")
print(person3.lastname) # Smith
print(person3.firstname)    # Sam
print(person3.fullname) # Sam Smith
person3.travel("Busan", "Yoda") # Sam Smith is traveling Busan with Yoda
person3.love(person2)   # Sam Smith is going out with Jisung Park
person3+person2     # Sam Smith married Jisung Park
person3.fight(person2)  # Sam Smith is fighting with Jisung Park
person3-person2 # Sam Smith divorced Jisung Park