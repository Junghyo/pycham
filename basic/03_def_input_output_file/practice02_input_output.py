"""
 input - output

 사용자 입력 → 처리(프로그램, 함수 등) → 출력

"""

# 1. using input
a = input()
print("입력받은 값:", a)

"""
 input("prompt")
"""

age = input("put your age: ")  # console창에  "put your age:" 문구가 뜸
print("your age:", age)

num1 = int(input("put the num1: "))
num2 = int(input("put the num2: "))
sum = num1 + num2
print("{0} + {1} = {sum}".format(num1, num2, sum=sum))


"""
 print 자세히 알기
"""
# 1. 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")
print("life"+"is"+"too short")

# 2. 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

# 3. 한 줄에 결과값 출력하기
for i in range(1, 11):
    print(i, end=" ")