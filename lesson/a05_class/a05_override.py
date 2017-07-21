'''
Created on 2017. 7. 21.

@author: kitcoop
메서드 오버라이딩
상속관계에 있어서, 하위클래스에서 상위클래스의 메서드를
동일한 이름으로 재정의하는 것을 말한다.
'''
class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self): ##method overriding
        print("아이1 호출됨!!!")
    
class Child2(Parent):
    def pringData(self):
        print("아이2 호출됨!!!") 
        print("부모는 같으나 다른 내용 정의")
        
c1 = Child1()
c1.printData()

c2 = Child2()
c2.pringData()

print("다형성 처리 확인")             
par = Parent()
par = c1 ## 폴리몰리즘 처리..
par.printData()

par = c2
par.pringData()
             
print("다형성 배열 처리..")
plist =[c1, c2]
for item in plist:
    item.printData()             
'''
@@@ 연습예제
상위클래스 :
    쓸것이라는 클래스 정의
        메서드 : writingSomething()
            
하위클래스
    볼펜  볼펜으로 사인을 하다.
    연필  연필로 뎃생을 그리다..

다형성 배열...    
'''   
class Writer:
    def writingSomething(self):
        pass
class BallPen(Writer):
    def writingSomething(self):
        print("볼펜으로 사인을 하다!!")

class Pencil(Writer):
    def writingSomething(self):
        print("연필로 뎃생을 그리다")

w1 = BallPen()
w2 = Pencil()        
wrlist = [w1, w2]

for wri in wrlist:
    wri.writingSomething()        

        
        
            
