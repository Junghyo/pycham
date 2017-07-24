'''
Created on 2017-07-21 18:01

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
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

"""
kor = int(input("국어성적을 입력하세요\n"))
eng = int(input("영어성적을 입력하세요\n"))
math = int(input("수학성적을 입력하세요\n"))
avg = (kor+eng+math)/3.0
print("== 성적표 ==")
print("국어: ", format(kor, "4d"))
print("영어: ", format(eng, "4d"))
print("수학: ", format(math, "4d"))
print("평균: ", format(avg, "4.1f"))
if avg >= 70:
    print("pass")
else:
    print("좀 더 노력하세요")


# 구구단 y가 3이면 출력안하고 8단 5에서 멈추기
for x in range(2, 10):
    print("%i단" % x)
    for y in range(1, 10):
        if y == 3: continue
        if x == 8 and y == 5: break
        print(x * y, end= ' ')
    if x == 8: break
    print(" ")

'''
확인예제..
입력으로 주민번호 입력
생년월일 :  @@@ 년 @@ 월 @@ 일
성별 :  남자/여자

'''
"8904151111111"
code = input()
year = "19" + code[0:2]
month = code[2:4]
day = code[4:6]
gender = code[7]
genderVal = "기타(외국인)"
if gender == "1":
    genderVal = "남자"
if gender == "2":
    genderVal = "여자"

print("생년월일 : {0}년 {1}월 {2}일".format(year, month, day))
print("성별: ", genderVal)
