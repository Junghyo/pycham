'''
Created on 2017. 7. 21.

@author: kitcoop
연산자 중복

'''
class AddClass:
    def __init__(self, s):
        self.s =s
    ## __add__부분은 클래스에 연산자(+)를 수행했을 때 수행되는 메서드..    
    def __add__(self,b):
        return "더하기 결과는 "+ str(self.s + b)
c = AddClass(5)
print(c+5)        
c2 = AddClass("kbs")
print(c2+" sbs")

class Gstring:
    def __init__(self, iniData):
        self.content=iniData
    ## 해당 객체에 - 연산자를 뒤에 붙을 때 처리될 내용..
    ##  ABCEDAABB    객체-A --> BCEDBB
    def __sub__(self, ss):
        for i in ss :
            self.content = self.content.replace(i, '')
        return Gstring(self.content)
    ## abs()함수를 적용했을 때, 처리될 내용
    def __abs__(self):
        return Gstring(self.content.lower())
    
    def print_data(self):
        print(self.content)
 
g = Gstring("ABCEDAABB")
g.print_data()
g = g-"AB"
g.print_data()
 
g = abs(g)
g.print_data() 
        
    
        

