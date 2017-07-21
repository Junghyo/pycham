'''
Created on 2017-07-21 13:57

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 super() : 자식class에서 부모class의 내용을 사용하고 싶을 경우
"""

class Father:
    def handsome(self):
        print("handsome")

class Son(Father):
    pass

class Daughter(Father):
    def pretty(self):
        print("pretty")

    def handsome(self):
        super().handsome()    # super()로 선언해주어야 출력이 된다.


father = Father()
father.handsome()

son = Son()
son.handsome()

daughter = Daughter()
daughter.handsome()
daughter.pretty()

print("-" * 50)

class Father:
    def __init__(self, who):
        self.who = who
    def handsome(self):
        print("handsome like {}".format(self.who))

father = Father("Daddy")

class Son(Father):
    def __init__(self, who, where):
        super().__init__(who)
        self.where = where

    def choice(self):
        print("Which part ? My {}".format(self.where))

    def handsome(self):
        super().handsome()
        self.choice()

son = Son("Daddy", "face")
son.handsome()

print("-" * 50)

"""
 class 2개 이상 상속
"""
class A () :
  def who(self) :
    print ("I am A")

class B () :
  def who(self) :
    print ("I am B")

class C (A, B) :
   pass
class D (B, A) :
   pass

c = C()
c.who() # I am A
d = D()
d.who() # I am B

print("-" * 50)

class Singer:
    def sing(self):
        return "la~la~la"

jackson = Singer()
print(jackson.sing())

print("-" * 50)

class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print("delicious!")

    def sleep(self):
        print("good-night!")

    def talk(self):
        print("bula-bula")

class Student(Person):
    def study(self):
        print("be smart!")

lee = Student()
print(lee.arms)
lee.eat()
lee.sleep()
lee.talk()
lee.study()

print("-" * 50)

class Fridge:
    isOpend = False
    foods = []

    def open(self):
        self.isOpend = True
        print("open the fridge !")

    def put(self, thing):
        if self.isOpend:
            self.foods.append(thing)
            print("put %s into the fridge !" % thing)
        else:
            print("impossible cause the fridge is closed")

    def close(self):
        self.isOpend = False
        print("close the fridge !")



f = Fridge()
f.open()
f.put("apple")
f.close()
f.put("elephant")
f.open()
f.put("banana")
f.put("elephant")
f.put("dog")
f.put("cat")
f.put("orange")
f.close()
print(f.foods)

print("-" * 50)

class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print("title : ", self.title)
        print("price : ", self.price)
        print("author : ", self.author)

    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print("using init")

    def __repr__(self):
        return self.title


b1 = Book("java", "$200", "ronaldo")
b1.printData()


b1.setData("python", "$300", "yoda")
b1.printData()

print(b1)

print("-" * 50)

class Shape:
    area = 0
    def __add__(self, other):
        return self.area + other.area

    def __cmp__(self, other):
        if self.area < other.area: return -1
        elif self.area == other.area: return 0
        else: return 1

a = Shape()
a.area = 20
b = Shape()
b.area = 30
print(a+b)  # 50
print(a.__add__(b)) # 50

print(a.__cmp__(b)) # -1
