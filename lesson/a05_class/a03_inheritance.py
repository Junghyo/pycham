'''
Created on 2017. 7. 21.

@author: kitcoop
'''

class Person:
    say = "안녕하세요"
    age = 30
    
    def __init__(self, age):
        print('생성자 호출')
        self.age = age
        
    def printInfo(self):
        print("나이:{}, 말하기:{}".format(self.age, self.say))
    
    def sayGoodBye(self):
        print("안녕히 가세요!!! 언제 만날려나??")    

print(Person.say, Person.age)

p = Person(22)
p.printInfo()
p.sayGoodBye()
## 상속처리..
### class 클래스명(상속클래스명)
class Employee(Person):
    say="일하는 사람"
    subject="근로자"
    
    def __init__(self):
        print("Employee 생성자")
        
    def ePrintInfo(self):
        self.printInfo()
        print(self.say, self.subject)
        self.sayGoodBye() 

e = Employee()
print(e.say, e.age)
e.ePrintInfo() 

class Worker(Person):
    def __init__(self, age):
        print("Worker 생성자")
        super().__init__(age)
    
    def wprintInfo(self):
        self.printInfo()    

w = Worker(25)
print(w.say, w.age)
w.wprintInfo()
w.printInfo()
'''



'''

       
    
          



