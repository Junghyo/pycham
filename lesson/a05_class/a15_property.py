'''
Created on 2017. 7. 24.

@author: kitcoop
'''
class Person:
    name="안녕맨"
    def __init__(self,sec="비밀"):
        print("person 호출")
        self.__sec=sec
        print("접근제어자 private 변수",self.__sec)
        
## 클래스 내부에서 사용될 member 변수가 필요할 때..
## __member 변수명..
    ## 접근제어자 있는 변수는 get/set 메서드로 선언 후, 접근..
    def getPosition(self):
        return self.__sec
    def setPosition(self,sec):
        self.__sec=sec  
## position이라는 이름으로 실제는 setPosition, getPosition을 통해서
## private 변수 sec를 할당하고자 할때, 이와 같이 쓰인다.          
    position1 = property(getPosition, setPosition) 
p01 = Person()  
print("이름:",p01.name)
p01.age=25
print("나이:",p01.age)
p02 = Person("비밀요원01")
print("이름:",p02.name)
## 해당변수는 접근이 안됨
##print("신분:",p02.__sec)
print("신분(정상 접근방법):",p02.getPosition())
p02.position1 = "비밀요원02"
print("신분(정상 접근방법):",p02.getPosition())



  