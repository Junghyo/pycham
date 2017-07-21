'''
Created on 2017. 7. 20.
확인예제(함수명 인수값 넘기기)
함수 calcu 정의
1. 연산기호 선택
2. 첫번째 값.
3. 두번째 값.
plus, minus, div, multi 함수 정의

연산기호에 따라 해당 함수 선택..
출력 양식 @@ 연산(+,-..) @@ = @@
@author: kitcoop
'''
def plus(*params):
    tot=params[0]+params[1]
    print(params[0]," + ",params[1]," = ",tot)  
def minus(*params):
    tot=params[0]-params[1]
    print(params[0]," - ",params[1]," = ",tot)
def multi(*params):
    tot=params[0]*params[1]
    print(params[0]," X ",params[1]," = ",tot)    
def div(*params):
    tot=params[0]/params[1]
    print(params[0]," / ",params[1]," = ",format(tot,"2.1f"))

def calcu(cal,num01,num02):
    if cal=="+":
        return plus(num01,num02)    
    if cal=="-":
        return minus(num01,num02)    
    if cal=="*":
        return multi(num01,num02)    
    if cal=="/":
        return div(num01,num02)  

calcu("+",25,72)      
calcu("-",33,27)      
calcu("*",25,72)      
calcu("/",5,3)      
    

    
    