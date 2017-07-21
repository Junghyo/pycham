'''
Created on 2017. 7. 19.

@author: kitcoop
'''

count =100 #정수 할당
weight = 25.7 # 실수 할당
name = "홍길동" # 문자열 할당
print("카운트:",count)
print("몸무게:",weight)
print("이름:",name)

num01 =5
num02 =2
print(num01**num02)
print(num01/num02)
print(num01//num02)

num03 = num04 = 25
num05, num06 = 75, 100

bool01 =True
bool02 = False

print( not( bool01 and bool02) )

cnt01 = 10
cnt02 = 20
list =[1,2,3,4,5]
print( cnt01,"이 포함 되어 있는지?",cnt01 in list )
print( cnt02,"이 포함 되어 않을 때?", cnt02 not in list )

num07 = 20
num08 = 20
print("같은지?",  num07 is num08)
print("다른지?",  num07 is not num08)
print("자료형1",type(num07))
print("자료형2",type(list))
print("저장위치",id(num08))
print("저장위치",id(list))

print(1,2); print(3,4)
print(1,2, end=' 마지막에 넣을 문자!! ');print(3,4)
print(1,2,3,4,5, sep="##")

print(format(4, '10d'))
print(format(43.2, '10.3f'))
print(format('안녕하세요1', '15s'),format('안녕하세요2', '15s'))
print("{0} is {1}".format("Python","Fun"))

name = input("이름:")
print("이름은 ", name)
num01 = int(input("첫번째 숫자를 입력:"))
num02 = int(input("두번째 숫자를 입력:"))
sum = num01+num02
print("{0} + {1} = {2}".format(num01,num02,sum))
