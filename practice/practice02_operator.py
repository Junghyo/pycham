"""
 # 연산자
 1. 산술연산자
 +, -, *, /
 제곱 : **
 나머지를 산출  : %
 몫 : //
"""

print("plus", 5 + 2)    # 7
print("minus", 5 - 2)   # 3
print("multiple", 5 * 2)    # 10
print("divide", 5 / 2)  # 2.5
print("square", 5 ** 2)  # 25
print("reminder", 5 % 2)    # 1
print("quotient", 5//2)  # 2

"""
 2. 비교 연산자
 ==, !=, <, >, <=, >=
"""
num = 10
if num == 1:
    print("num is 1")
else:
    print("num is not 1")

if num >= 1:
    print("num is more then 1")
else:
    print("num is less than 1")

"""
 3. 할당연산자
 +=, -=, *=, /=, %=, //=
"""
print(num * 10)  # 100
num *= 10
print(num)  # 100


"""
 4. 논리연산자
 and, or, not
 and : 양쪽 모두 참
 or  : 둘중 하나만 참
 not : 참이면 거짓, 거짓이면 참
"""
x = True
y = False
if x and y:
    print("yes")
else:
    print("no")

if x or y:
    print("yes")
else:
    print("no")

"""
 5. Bitwise 연산자
 &(AND), |(OR), ^(XOR), ~(Complement), <<, >>(Shift)
 비트단위의 연산을 하는데 사용
"""
a = 8
b = 11
c = a & b
d = a ^ b
e = a >> b
f = a << b
g = ~ b
h = ~ a
print(c)    # 8
print(d)    # 3
print(e)    # 0
print(f)    # 16384
print(g)    # -12
print(h)    # -9

"""
 6. 멤버쉽 연산자
 in, not in 
 좌측 Operand가 우측 Collection(List)에 속해 있는지 Check
"""
a = [1, 2, 3, 4]
if 3 in a:
    print("3 is in", a)
else:
    print("3 is not in", a)

if 10 not in a:
    print("10 is not in", a)
else:
    print("10 is in", a)

"""
 7. Identify 연산자
 is, is not
 양쪽 Operand가 동이한 Object인지 아닌지 Check
"""
a = "ABC"
b = a
print(a is b)  # True
b = "abc"
print(a is b)   # False
print(a is not b)   # True