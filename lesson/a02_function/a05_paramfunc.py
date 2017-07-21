'''
Created on 2017. 7. 20.

@author: kitcoop

함수의 인자값 처리..
def 함수명(지역변수1, 지역변수2 =default 데이터)

지역변수1은 첫번째 입력값..
지역변수2는 입력이 두번째 일때와,
   두번째 입력값이 없을 때는 해당 데이터로 할당.. 

'''
##  입력값, 1,2일 때, 두번째 값이 입력되지 않으면,
## 두번째 입력값을 default값은 5 처리..
def showGugu(start, end=5):
    for dan in range(start, end+1) :
        print(str(dan) + "단 출력")
        for i in range(1,10):
            print(str(dan) + " * " + str(i) + " = "+str(dan*i), end="\t")
        print()    

showGugu(2, 3)
showGugu(4) # 1개의 입력값만 있으면 end값은 default값으로 처리

showGugu(start=3, end=4)

showGugu(end=7, start=5)

## 가변 인수 처리..
## 함수의 인수값이 0~~ 여러개값으로 변화될 때, 활용된다.
### 형식 def 함수명(*가변변수list)
def Func1(*ar):
    print(ar)
    for obj in ar:
        print("food:"+obj)
    print()    

Func1("짜장면")        
Func1("짜장면","짬뽕")    

## 고정 인수, 가변 인수 혼합처리..
## def 함수명(지역변수명, *가변변수)
def Func2(a, *ar):
    print("첫번째값:",a)
    print("가변변수 list",ar)
    for obj in ar:
        print("food:"+obj)
 
Func2("ham","egg","spam")       
## 첫번째 인수조건에 따라서 달라지는  가변변수 처리..
def selfProc(choice, *ar):
    if choice == "sum":
        re=0
        for val in ar:
            re +=val
    if choice == "mul":
        re=1
        for val in ar:
            re *= val
    return re

print(selfProc("sum", 1,2,3,4,5))
print(selfProc("mul", 1,2,3,4,5))

## ndict인 경우
## **인수값, key=value형식으로 데이터를 입력할 때, 활용된다.
def Func3(w, h, **other):
    print("몸무게 {}, 키{}".format(w,h))
    print(other)                

Func3(65, 175, irum="지구인", nai=23)
Func3(63, 178, irum="한국인")
'''
def 함수명1(인자값1):
    처리할 내용
    
함수명2 = 함수명1

함수명2(인자값)    
'''            
def print_something(a):
    print("출력될 내용:",a) 

p = print_something;
p("홍길동")               

def plus(a, b):
    return a+b
def minus(a, b):
    return a-b

flist =[plus, minus]
print("함수명을 list할당 후, 사용1:",flist[0](1,2))            
print("함수명을 list할당 후, 사용2:",flist[1](1,2))            
'''
파이선의 함수는 일급 객체(First Class Object)로 다루기 때문에,
매개변수로 함수를 넘기거나, 반환처리가 가능..
'''            
def hello_korean():
    print("안녕하세요!!")
def hello_english():
    print("Hello")

## 함수명을 입력력을 전달 후, 처리..
def greet(hello1):
    hello1()
    
greet(hello_korean)   
greet(hello_english)   

## 조건에 따른 여러함수호출..
def get_greeting(where):
    if where == "K":
        return hello_korean
    else :
        return hello_english

hello = get_greeting("K")
hello()
hello = get_greeting("E")
hello()

## 축약함수(Lamda - 이름이 없는 한 줄짜리 함수)
## 형식 : Lambda 인자,, :표현식 <<== 인자와 표현식으로 return 한줄에 처리..

def hap(x, y):
    return x+y
print("합산된 결과",hap(25,7))
print("합산된 결과 람다로 처리..", (lambda x,y:x+y)(5,7))

defLam = lambda x,y:x*y
print("람다형식 출력:",defLam(27,5))
## 람다에서 가변 인수 사용
kbs = lambda a, su=10: a+su
print(kbs(5))
print(kbs(5,6))





    
    
 
                
        






