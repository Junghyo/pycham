'''
Created on 2017. 7. 21.
확인예제
Father
    weight=70
    play()
      운동을 잘함
    sound()
      노래를 잘함

Mother
   height=170
   study()
      공부를 잘함
   sound()
     노래를 못함.
위 두가지 클래스를 상속 받은 
son1
daughter1
에서 처리하는 내용 (메서드와, 재정의 활용)
@author: kitcoop
'''
class Father:
    weight =70
    def play(self):
        print("운동을 잘 함!")
    def sound(self):
        print("노래를 잘 함!")

class Mother:
    height=170
    def study(self):         
        print("공부를 잘 함")
    def sound(self):
        print("노래를 못 함")

class Son1(Father, Mother):
    def __init__(self):
        print('##아들!!')
class Daughter1(Mother, Father):
    def __init__(self):
        print("##딸!!")
        self.weight=55
    def sound(self):
        Father.sound(self)  
          
    def showAll(self):
        self.play()
        self.sound()
        self.study()        
             
c1 = Son1()
c1.play()
c1.sound()
c1.study()
c2 = Daughter1()
c2.showAll()               





