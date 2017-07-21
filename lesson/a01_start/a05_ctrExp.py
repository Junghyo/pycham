'''
Created on 2017. 7. 19.
확인예제..
input 활용하여, 국어, 영어, 수학 점수를 입력 받아서..
다음 형식으로 출력하고,
== 성적표 ==
국어 : @@@
영어 : @@@
수학 : @@@
총점 :  @@
평균 : @@(소숫점1자리)
평균이 70이상일 때, 
패스!!! 그외는 열심히 공부하세요..
@author: kitcoop
'''
kor = int(input("국어점수입력:"))
eng = int(input("영어점수입력:"))
mat = int(input("수학점수입력:"))
sum = kor+eng+mat
avg = sum/3.0
print("== 성적표 ==")
print("국어 : ",format(kor,"4d"))
print("영어 : ",format(eng,"4d"))
print("수학 : ",format(mat,"4d"))
print("총점 : ",format(sum,"4d"))
print("평균 : ",format(avg,"4.1f"))
if avg>=70 :
    print("PASS!")
else :
    print("열심히 공부하세요!")    


