'''
Created on 2017. 7. 20.

@author: kitcoop
확인예제(내장 함수 처리)

아버지의 약속
 성적표 5과목 list 형식으로 처리..
 1. 한과목이라도 100점이 있으면, 상금 5만원 획득..
 2. 모든 과목이 70점 이상이면, 상금 3만원 획득
 3. 평균점수과 80점 이상이면, 상금 4만원 획득.
 4. 점수 list에 과목명 듀플로 생성..
     점수와 과목이 매핑된 듀플 출력..
'''
points =[90,80,70,62,100]
print("성적표:", points)

print("1.한과목 이라도 100점? ")
if any(point==100 for point in points):
    print("상금 5만원 획득!!")
else :
    print("상금 5만원 획득 실패!!")  
print("2.모든 과목이 70점이상 ")
if  all(point>=70 for point in points):
    print("상금 3만원 획득!!")
else :
    print("상금 3만원 획득 실패!!")  
print("3.평균이 80점이상 ")
print("평균:",format(sum(points)/5.0,"2.1f"))
if sum(points)/5.0>= 80:
    print("상금 4만원 획득!!")
else :
    print("상금 4만원 획득 실패!!")  
subjects =["국어","영어","수학","과학","미술"]
print("과목","점수")
for data in zip(subjects, points):
    print(data[0],format(data[1],"3d"))
        
    
    
    
      