'''
Created on 2017. 7. 21.

@author: kitcoop

다중 상속:파이슨에서는 상위 클래스를 다중으로 상속이 가능하다.
'''
class Tiger:
    data ="동물의 세상"
    def cry(self):
        print("호랑이 어흥")
    def eat(self):
        print("맹수는 고기를 좋아함!")

class Lion:
    def cry(self):
        print("사자 어르렁")            
    def hobby(self):
        print("야수는 낮잠이 취미임") 

## 다중 상속 : 두가지 클래스를 상속해서 사용함..
class Liger01(Lion, Tiger):
    pass

class Liger02(Tiger, Lion):
    def play(self):
        print("라이거는 즐겁게 논다")
        super().hobby()
    
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data+", ", super().data)
 
l1 = Liger01()
l1.cry()
l1.eat()
print("Liger02####")
l2 = Liger02()
l2.cry()
l2.eat()
l2.hobby()
l2.play()
l2.hobby() 

print("라이거2에 showhobby")
l2.showHobby()

print(Liger02.__mro__)
'''
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


'''
