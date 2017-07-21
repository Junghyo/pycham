'''
Created on 2017. 7. 19.

@author: kitcoop
'''
str="Korea"
print(str[0])
print(str[-2])
print(str[1:3])
print(str[0:5:2])
print(str[:-1])
print(str[::-1])
'''
확인예제..
입력으로 주민번호 입력
생년월일 :  @@@ 년 @@ 월 @@ 일
성별 :  남자/여자

'''
civilnum = input("주민번호입력")
biryear = "19"+civilnum[0:2]
birmon = civilnum[2:4]
birdate = civilnum[4:6]
gender = civilnum[7]
genderStr="기타(외국인등)"
if gender =="1":
    genderStr="남자"
if gender =="2":
    genderStr="여자"
print("생년월일 : {0}년 {1}월 {2}일".format(biryear,birmon,birdate))
print("성별 : ", genderStr)    



