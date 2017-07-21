'''
Created on 2017. 7. 21.

@author: kitcoop

filter 내장 함수
 컬렉션과 함수를 매개변수로 받아, 컬렉션의 모든 데이터를 함수의 매개변수로
 대입해서 결과가 참인 경우만 리턴하는 함수..
 filter(함수-람다, 컬렉션-리스트형태객체)

'''
li=[1,2,3,4,5]
result = list(filter(lambda x:x%2==0, li))
print("결과값:",result)
'''
확인예제
1. 국어, 영어, 수학 점수의 리스트를 있다.
    국어 : 60 70 80
    영어 : 90 100 70
    수학 : 50 60 70
    
2. 국어, 영어, 수학 점수의 평균이 70이상인 
데이터만 평균 list를 출력 하세요..
'''
kor =[60,70,80]
eng =[90,100,70]

mat =[50,60,70]

def mkavg(k,e,m):
    return (k+e+m)/3
avglist = list(map(mkavg,kor,eng,mat))
print(avglist)
result = list(filter(lambda x:x>=70,avglist))
print(result)





