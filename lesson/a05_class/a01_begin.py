'''
Created on 2017. 7. 21.

@author: kitcoop
'''
class Car:
    handle = 1  ## 멤버 변수는 전역
    speed = 0
    kind = "자동차종류"
    airBag=0
    ## 생성자.. 초기화 할때..
    '''
    def __init__(self):
        print("초기 생성자")
        self.kind="그렌저"
    '''    
    def __init__(self, airBag, kind): 
        self.airBag = airBag  
        self.kind = kind
        
    ### 멤버 메서드 정의..
    def setSpeed(self, speed):
        self.speed+=speed
        
    def getSpeed(self):
        return self.speed   
    
    ### 소멸자..: 객체가 메모리에 삭제 될 때 호출됨..
    ### 메모리자 자동관리되므로 사용빈도 낮다.
    def __del__(self):
        print("소멸자 호출!! 자원 해제됩니다.")
    
         

##car01 = Car()
##print(car01.kind)
car02 = Car(1,"제규어")
print(car02.airBag, car02.kind)
car02.setSpeed(5)
car02.setSpeed(5)
car02.setSpeed(5)
print("속도",car02.getSpeed())
## 자원 메모리 해제, 소멸자 호출..
del car02




