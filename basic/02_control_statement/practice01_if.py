"""
 if( conditional statement )

 if 조건문:
     수행할 문장1
     수행할 문장2
     ...
 else:
     수행할 문장A
     수행할 문장B
     ...

 if 조건문 뒤에는 반드시 콜론(:)이 붙는다.


"""

# ex 1. If you have money $3000, get on the cab. or just walk.
print("=" * 50)
print("ex 1. If you have money $3000, get on the cab. or just walk.")
print("=" * 50)
money = 2000
print(money)
if money >= 3000:
    print("get on the cab.")
else:
    print("just walk!")
# just walk!
# money >= 3000이 false가 되기 때문에 else statement를 수행

"""
 and, or, not

 연산자	            설명
 x or y	            x와 y 둘중에 하나만 참이면 참이다
 x and y	        x와 y 모두 참이어야 참이다
 not x	            x가 거짓이면 참이다 
 
"""

# ex 2. If you have money 3000 or card, get on the cab. or just walk.
print("=" * 50)
print("ex 2. If you have money 3000 or card, get on the cab. or just walk.")
print("=" * 50)

money = 2000
card = "have"
print(money)
print(card)

if money >= 3000 or card:
    print("get on the cab.")
else:
    print("just walk.")

"""
 x in s, x not in s
 
 in	            not in
 x in list	    x not in list
 x in tuple	    x not in tuple
 x in string	x not in string
"""
print("=" * 50)

print("a" in "ronaldo")   # True
print(1 not in [1, 2, 3])   # False
print("j" in ("a", "b", "c"))   # False

# ex3. if you have money in your pocket, get on the cab.
print("=" * 50)
print("ex3. if you have money in your pocket, get on the cab.")
print("=" * 50)

pocket = ["paper", "cellphone", "money"]
print(pocket)   # ['paper', 'cellphone', 'money']
if "money" in pocket:
    print("get on the cab.")
else:
    print("walk.")
# get on the cab.

"""
 if statement using pass
"""
# ex4. if you have money in your pocket, keep standing. or take a card
print("=" * 50)
print("ex4. if you have money in your pocket, keep standing. or take a card")
print("=" * 50)

print(pocket)

if "money" in pocket:
    pass
else:
    print("take a card.")
# 아무런 수행도 하지 않음.

"""
 다양한 조건을 판단하는 elif
if <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
   
"""
# ex5. you have money, get on the cab. you don't have money but have a card, get on the cab. or walk.
# if와 else 만으로 처리
print("=" * 50)
print("using if~else")
print("=" * 50)

pocket = ["paper", "cellphone"]
print(pocket)
print(card)
if "money" in pocket:
    print("money : get on the cab.")
else:
    if card:
        print("card : get on the cab.")
    else:
        print("walk.")
# card : get on the cab.

print("=" * 50)
print("ex5. using elif")
print("=" * 50)

print(pocket)
print(card)

if "money" in pocket:
    print("money : get on the cab.")
elif card:
    print("card : get on the cab.")
else:
    print("walk.")
# card : get on the cab.

"""
 if문을 한줄로 작성하기
"""
print("=" * 50)
# solve ex4.
pocket = ['paper', 'money', 'cellphone']
print(pocket)
print(card)

if "money" in pocket: pass # if와 같은 줄에 수행할 문장을 바로 적어줌
else: print("take a card")