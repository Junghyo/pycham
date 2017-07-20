"""
 for( loop statement )

 for 변수 in list(또는 tuple, string):
    수행할 문장1
    수행할 문장2
    ...

"""

"""
 for statement basic
"""

# ex1. for loop using list 1
print("=" * 50)
print("ex1. for loop using list 1")
print("=" * 50)

test_list = ["one", "two", "three", "four"]
print(test_list)

for i in test_list:
    print(i)
# one
# two
# three
# four

# ex2. for loop using list 2
print("=" * 50)
print("ex2. for loop using list 2")
print("=" * 50)

a = [(1, 2), (3, 4), (5, 6)]
for (x, y) in a:
    print("%i + %i = %i" % (x, y, x+y))
# 1 + 2 = 3
# 3 + 4 = 7
# 5 + 6 = 11


# ex3. for loop using dict
print("=" * 50)
print("ex3. for loop using dict")
print("=" * 50)
a = {"name": "ronaldo", "age": 32, "team": "real madrid"}
for i in a:
    print("key(", i, ") : value(", a[i], ")")
# key( name ) : value( ronaldo )
# key( age ) : value( 32 )
# key( team ) : value( real madrid )


# ex4. application for loop
print("=" * 50)
print("ex4. application for loop")
print("=" * 50)

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여주시오.

score = [90, 25, 30, 60, 75, 80, 55]
number = 0
for i in score:
    number += 1
    if i >= 60:
        print("%i 번째 학생은 합격입니다." % number)
    else:
        print("%i 번째 학생은 불합격입니다." % number)

# ex5. for loop using continue
print("=" * 50)
print("ex5. for loop using continue")
print("=" * 50)

# 100명의 사람들 중 10의 배수 사람들에게 당첨 메세지 보내기
for x in range(1, 101):
    if x % 10 != 0: continue
    print("%i 번째 분, 당첨되셨습니다. 축하드립니다." % x)

"""
 for와 함께 자주 사용하는 range함수
"""
# ex6. for loop using range
print("=" * 50)
print("ex6. for loop using range")
print("=" * 50)

a = range(10)
print(a)    # range(0, 10) 0 이상 10 미만. 끝 숫자는 포함되지 않음

# 1~10 까지 숫자 더하기
sum = 0
for x in range(1, 11):
    sum += x
print(sum)  # 55


# using ex4
score = [90, 25, 30, 60, 75, 80, 55]
for num in range(len(score)):
    if score[num] >= 60:
        print("%d 번째 학생 합격입니다." % (num+1))
    else:
        print("%d 번째 학생 불합격입니다." % (num+1))


# ex7. multiplication table using for, range
print("=" * 50)
print("ex7. multiplication table using for, range")
print("=" * 50)

for dan in range(2, 10):
    print("%d단" % dan)
    for grade in range(1, 10):
        print("%d X %d = %d " % (dan, grade, dan*grade), end=" ")
    print('')

"""
[입력 인수 end를 넣어 준 이유는 무엇일까?]

앞의 예제에서 print(i*j, end=" ")와 같이 입력 인수 end를 넣어 준 이유는 
해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다.
그 다음에 이어지는 print(' ')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면
결과값을 다음 줄부터 출력하게 해주는 문장이다.
"""

"""
list 안에 for문 포함하기 : list comprehension

list = [표현식 for 항목 in 반복가능객체 if 조건]
"""
# ex8. list comprehension( for loop )
print("=" * 50)
print("ex8. list comprehension( for loop )")
print("=" * 50)

# ex 8-1. list a에 3을 곱한 값으로 list 만들기
a = [1, 2, 3, 4]
result = []
for x in a:
    result.append(x*3)
print(result)

result = [data*3 for data in a]
print(result)
# 두 logic이 같은 값을 출력

# ex 8-2. list a에서 짝수들만 3을 곱한 값으로 list 만들기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x*3 for x in a if x % 2 == 0]
print(result)   # [6, 12, 18, 24, 30]

# ex 8-3. 구구단 list에 담기
result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)