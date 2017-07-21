'''
Created on 2017. 7. 20.

@author: kitcoop
내장함수 : 파이선 자체에서 자원하는 함수
sum(), bin(), int(), float(), str()
'''
print("내장 함수")
print(sum([3,5,7]))
print(sum((3,5,7)))
print(sum({3,5,7}))
# print(sum(3,5,7)) : 해당 내용은 배열형태가 아니기에.
# 에러 발생..
print("2진수 처리 0b@@@@ :",bin(8));
## print(5+"오") 형변환이 필요하다(숫자 --> 문자열)
print(int(1.7), float(5), str(5)+"오!!")

a = 10
b = eval("a + 5")
## eval() 안 있는 문자열은 변수의 내용으로 인식해서..
## 프로그램적으로 처리한다. 
print(b)

print(round(1.2), round(1.7))
import math
print(math.ceil(1.2), math.ceil(1.6))
print(math.floor(1.2), math.floor(1.6))

b_list =[True, 1, False]
## all() : 모두가 bool값이 true일 때, true return
## any() : 하나가 true 이면, true로 return
print(all(b_list))
print(any(b_list))
b_list2 =[1,3,2,5,7,6]


## 배열형식의 데이터가 모두가 조건 맞을 때..
re = all( a < 10  for a in b_list2)
print("모두가 10 이하 인지?",re)
## 배열형식의 데이터의 하나라도 조건 맞을 때..
re = any( a < 3 for a in b_list2)
print("숫자 중 3미만이 있는지?", re)

## zip() 복수 개의 리스트로 듀블을 작성..
x=[10,20,30];
y=["a","b"]
for i in zip(x,y) :
    print(i)







