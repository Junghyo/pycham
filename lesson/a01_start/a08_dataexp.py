'''
Created on 2017. 7. 19.

@author: kitcoop
'''
name=input("이름:")
weight=int(input("몸무게 입력"))
print("## 헬스 트레이닝 ##")
print("이름 :", name)
print("현재 몸무게 :", weight)
print("목표 몸무게 :", format(weight-(weight*0.1),"3.1f"))
import math
print("목표 몸무게(내림) :", math.floor(weight-(weight*0.1)))
from fractions import Fraction
num01 = Fraction(5,7)
print(num01)
num02 = Fraction(5,3)
print(num02)
print("합산", num01+num02)

