'''
Created on 2017-07-27 09:59

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 객체를 파일로 저장할 떄, 장점
 1) 파일에 특정데이터를 로딩하지 않고도 객체 단위로 바로 활용
 
 python에서 객체를 파일로 저장 할 때, 사용되는 모듈
 1) 피클링 모듈, DBM 관련 모듈
 2) 피클링모듈은 임의의 python 객체를 저장하는 가장 일반화된 모듈
 
 피클링(pickle)을 통한 저장처리
 1) pickle.dump(출력할 객체, 파일객체)
 
 피클링을 통해 읽어오기
 1) pickle.load(파일객체) : 객체를 1개씩 읽기
 2) pickle.loads(파일객체) : 객체 전체를 바이트 단위로 읽기
"""

import numpy as np

class Dto:
    def setNum(self, num):
        self.num = num
    def setName(self, name):
        self.name = name
    def getNum(self):
        return self.num
    def getName(self):
        return self.name
    def toString(self):
        return {"number": str(self.num), "name": self.name}


data1 = Dto()
data1.setNum(114)
data1.setName("park")

data2 = Dto()
data2.setNum(227)
data2.setName("Ronaldo")

l = [data1, data2]

import pickle

# 반복문을 통해서 여러 객체를 한 파일에 할당할 경우
# with open(파일) as 파일객체명:
#   pickle.dump(data, 파일객체명)
with open("test_pickle.txt", "wb") as f:
    pickle.dump(l, f)
f.close()

with open("test_pickle.txt", "rb") as f:
    data = pickle.load(f)
    for temp in data:
        print(temp.toString())

"""
 ex)
 Person calss
    name, age (set/get)
  
  2명 파일 저장 및 로딩처리
"""

class Person:
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def intro(self):
        return {"name": self.name, "age": str(self.age)}

p1 = Person()
p1.setName("Yoda")
p1.setAge(29)
p2 = Person()
p2.setName("Messi")
p2.setAge(32)

l2 = [p1, p2]
with open("test_pickle2.txt", "wb") as f:
    pickle.dump(l2, f)

f.close()

with open("test_pickle2.txt", "rb") as f:
    data = pickle.load(f)
    for temp in data:
        print(temp.intro())