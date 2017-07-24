'''
Created on 2017. 7. 21.

@author: kitcoop
'''
from abc import *
                
class Robot(metaclass=ABCMeta):
    attList=""
    defList=""
    kind=""
    def __init__(self,kind):
        self.kind=kind
            
    @abstractclassmethod
    def attack(self):
        pass
    @abstractclassmethod
    def defend(self):
        pass
    def fight(self):
        self.attack()
        self.defend()     
   


class Mz(Robot):
    def __init__(self):
        super().__init__("MZ")
        self.attList="로켓주먹 "
        self.defList="방어막형성 "
        
    def attack(self):
        print(self.kind+" 로봇이")
        print(self.attList+" 으로 MZ공격을 한다")
        
    def defend(self):
        print(self.kind+" 로봇이")
        print(self.defList+" 으로 MZ방어를 한다")   
    def __add__(self,skill):
        print("공격방법 추가")
        self.attList+=skill+" "
        print("현공격방법:"+self.attList)
        
    def __sub__(self,skill):
        print("공격방법 제거")
        self.attList = self.attList.replace(skill, '')
        print("현공격방법:"+self.attList)   
                                  
    
class Gandam(Robot):
    def __init__(self):
        super().__init__("GANDAM")
        self.attList="변신공격 "
        self.defList="방어막형성 "
        
    def attack(self):
        print(self.kind+" 로봇이")
        print(self.attList+" 으로 GANDAM공격을 한다")
        
    def defend(self):
        print(self.kind+" 로봇이")
        print(self.defList+" 으로 GANDAM방어를 한다")     
        
    def __add__(self,skill):
        print("공격방법 추가")
        self.attList+=skill+" "
        print("현공격방법:"+self.attList)
        
    def __sub__(self,skill):
        print("공격방법 제거")
        self.attList = self.attList.replace(skill, '')
        print("현공격방법:"+self.attList)            
    
r1 = Mz()
r2 = Gandam()
r1+"레이저빔"
r1.fight()
r1-"로켓주먹" 
r1.fight()



rlist =[r1, r2]

for robot in rlist:
    robot.fight()

   
     