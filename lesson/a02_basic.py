
import keyword
print(keyword.kwlist)

count = 100  # 정수 할당
weight = 25.7  # 실수 할당
name = "호날두"  # 문자열 할당
print("count:", count)
print("weight:", weight)
print("name:", name)

num01 = 5
num02 = 2
print(num01**num02)
print(num01/num02)
print(num01//num02)

num03 = num04 = 25
num05, num06 = 75, 100
boo01 = True
boo02 = False
print(not(boo01 and boo02))
print(num03 != num04)
print(num05 + num06)

cnt01 = 10
cnt02 = 20
list = [1, 2, 3, 4, 5]
print(cnt01, "이 포함되어 있는가?", cnt01 in list)
print(cnt02, "이 포함되어 있지 않은가?", cnt02 not in list)

num07 = 20
num08 = 20
print(num07, "과 ", num08, "은 같은가?", num07 is num08)
print(num07, "과 ", num08, "은 다른가?", num07 is not num08)

print(format(4, "10d"))
print(format(43.3, "10.3f"))
print(format("안녕하세요!", "10s"), format("반갑습니다", "10s"))
print('{0} is {1}'. format("Python", "Fun"))

var1 = 100
if var1:
    print("1 - true 일 때 수행될 문장")
    print(var1)

var2 = 0
if var2:
    print("2 - true 일 때 수행될 문장")
    print(var2)
print("goody-bye")
