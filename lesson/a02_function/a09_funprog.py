'''
Created on 2017. 7. 21.

@author: kitcoop
map 내장 함수
  컬렉션과 함수를 매개변수로 받아서 컬렉션의 모든 데이터를
  함수의 매개변수로 대입해서 결과를 리턴하는 함수.

'''
def f(x):
    return x*x

li =[1,2,3,4,5]
print("반복문을 이용하여 실행")
for imsi in li:
    print(f(imsi), end=" ")
print("\nMap을 이용한 실행")
## map(함수명, 배열형태객체)
## 위 내용 list형태로 type casting
result = list(map(f, li))
print(result)
print("lambda와 map을 이용한 실행")
result = list(map(lambda x:x*x, li))
print(result)





    

    


