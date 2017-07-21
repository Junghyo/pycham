'''
Created on 2017. 7. 21.

@author: kitcoop
추상클래스..
'''
from abc import *


class AbstractClass(metaclass=ABCMeta): ## 추상클래스
    
    ## 추상메서드 선언..
    @abstractclassmethod
    def absMethod(self):
        pass
    
    def normalMethod(self):
        print("추상클래스 내에 일반 메소드")
        
##b = AbstractClass() 추상클래스 단독으로 객체생성을 할 수 없음..
class Chil1(AbstractClass):
    
    def absMethod(self):
        print("추상 메서드를 오버라이딩 함!!")
        
c1 = Chil1()
c1.absMethod()
c1.normalMethod()
        
print("##"*25)
class Friend(metaclass=ABCMeta):
    def __init__(self, name):
        self.name=name
    @abstractmethod
    def hobby(self):
        pass
    
    def printName(self):
        print("name:"+self.name)

class Tom(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr=addr
    
    def hobby(self):
        print(self.addr+" 거리를 걸어다님")
        
    def printAddr(self):
        print("주소는 "+ self.addr)
        
class James(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr=addr
    
    def hobby(self):
        print(self.addr+" 거리를 뛰어다님")
        
    def printAddr(self):
        print("사는 곳는 "+ self.addr)
                
tom = Tom("톰","강남")
tom.printName()
tom.printAddr()
tom.hobby()

james = James("제임스", "종로")
james.printName()
james.printAddr()
james.hobby()
        
        
        
                    
        
        
        

        
