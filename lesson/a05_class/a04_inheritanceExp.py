'''
Created on 2017. 7. 21.

@author: kitcoop
상속처리

탈것 Vehicle
속성: 종류, 탑승자수
생성자를 통해서 종류가 할당
메서드 : 
1) 탑승자수를 할당..
2) gogo()
   @@@을 @@@명이 타고 갑니다.

상속 Car
속성 : speed
생성자 : 탑승자수, speed를 할당
         상위 생성자 호출..
메서드..
  drive()
    상위 gogo() 호출..
    시속 @@@로 달린다.

'''
class Vehicle:
    passcnt=0
    def __init__(self,kind):
        self.kind=kind
    
    def setRidecnt(self,passcnt):
        self.passcnt=passcnt
    
    def gogo(self):
        print(self.kind,"를 ",self.passcnt,"명이 타고 갑니다")
 
class Car(Vehicle):
    speed=0
    def __init__(self, passcnt, speed):
        super().__init__("자동차")
        super().setRidecnt(passcnt)
        self.speed=speed
    def drive(self) :
        super().gogo()
        print("시속 ",self.speed,"km로 달린다")
        
print("상위 클래스")
v1 =Vehicle("버스")  
v1.setRidecnt(5)
v1.gogo()  
print("하위 클래스")
v2 = Car(3,100)
v2.drive()    
 
            