'''
Created on 2017. 7. 20.

@author: kitcoop

사용자 정의 함수..
형식
def 함수명(인수1, 인수2,...):
    구문...
    return <반환값>

'''
def doFuc1():
    print("함수1 호출")
doFuc1()
def doFuc2(name):
    print(name," 반습니다!")
doFuc2("홍길동")

def doFuc3(arg1, arg2):
    re = arg1 + arg2
    return re
num01 = 25
num02 = 30
sum = doFuc3(num01, num02)
print(num01," + ", num02, " = ", sum)

## 함수에서 함수를 호출 해서 처리..
def Area_print(c):
    print("삼각형의 면적은 ", c)
## 함수호출
def Area_tri(a, b):
    c = a * b/2
    Area_print(c)
    
Area_tri(20, 30)

'''
지역, 전역 변수
변수 영역 및 접근 순서
Local >  Enclosing function > Gobal > Built_in

'''
plyer = "전국대표" # 전역변수..
def FuncSoccer():
    name="홍길동" #  지역 변수..
    plyer="지역 대표" # 전역/지역 변수-->전역변수에 데이터를 할당 처리..
                    # 주석하면 전역변수에 할당된 내용을 볼 수 있다.
    print(name, plyer)

FuncSoccer()   
# global : 전역변수의 내용을 명시적으로 처리하기 위해 사용되는 keyword
a = 10; b=20; c=5
def Foo():
    a = 30
    def Bar():
        global a
        a =3
        c = 40
        print("L:{}, E:{}, G:{}".format(c,a,b))
    Bar()
    print("a는 ",a)
    a=50
    print("a는 ", a)
    
Foo()  
print("Foo 수행 후 a:",a)   
## 변수 영역의 이해..
v1 =1
def varTest(v1):
    v1 =v1+1
    print("지역:",v1)
varTest(v1) # 전역변수의 할당된 데이터값만 넘기..
            # 전역변수의 값이 변하지 않는다..
            
print("전역변수:",v1)

def varTest2(v2):
    v2 =v2 +1
    print("지역:", v2)
varTest2(5)
#print(v2) : v2지역 변수이기에 에러가 발생!!
   
g = 1
def Func():
    global g
    a = g
    g = 2
    return g

print("함수호출:",Func())
print("전역 변수 g:", g)

    

      



    

    

    
    
    

