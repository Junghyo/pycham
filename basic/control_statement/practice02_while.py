"""
 while( loop statement )

 조건문이 true인 동안 while 안의 문장들을 반복해서 수행한다.

 while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...

"""

# ex1. 열 번 찍어 안 넘어 가는 나무 없다.
print("=" * 50)
print("ex1. 열 번 찍어 안 넘어 가는 나무 없다.")
print("=" * 50)
treeHit = 0

while treeHit <10:
    treeHit += 1
    print("%d hit the tree!" % treeHit)
    if treeHit == 10:
        print("the tree falls!")
# 1 hit the tree!
# 2 hit the tree!
# 3 hit the tree!
# 4 hit the tree!
# 5 hit the tree!
# 6 hit the tree!
# 7 hit the tree!
# 8 hit the tree!
# 9 hit the tree!
# 10 hit the tree!
# the tree falls!

"""
 make while statement by myself
"""
# ex2. 선택지를 만들어서 입력받는 예제 : input
print("=" * 50)
print("ex2. 선택지를 만들어서 입력받는 예제 : input")
print("=" * 50)
prompt = '''
1. Add
2. Del
3. List
4. Quit
...
    Enter number: 
'''
number = 0
data = []
while number != 4:
    print(prompt)
    number = int(input())
    if number == 1:
        data.append("a")
    elif number == 2:
        del data[-1]
    elif number == 3:
        print(data)
# 1번 누르면 data에 a가 추가되고 2번 누르면 data의 마지막 index가 삭제
# 3번을 누르면 list가 보여지고 4번 누르면 while문 종료

"""
 while문 강제로 빠져나가기 : break
"""
# ex3. coffee vending machine 1
print("=" * 50)
print("ex3. coffee vending machine 1")
print("=" * 50)

coffee = 10     # 커피 수량
money = 300     # 보유 money
price = 20      # 커피 가격

while money:
    print("coffee's price: $%d" % price)
    coffee -= 1
    print("coffe's quantity: %d" % coffee)
    money -= price
    print("the money left: $%d" % money)
    print("-" * 50)
    if not coffee:
        print("sold out! stop the sale of coffee.")
        break

# ex4. coffee vending machine 2
print("=" * 50)
print("ex4. coffee vending machine 2")
print("=" * 50)

coffee = 10     # 커피 수량
price = 300     # 커피 가격
while True:
    x = input("put the money!\n")
    try:
        money = int(x)
        if money == 300:
            print("take your coffee")
            coffee -= 1
            print("coffee's quantity: %i" % coffee)
            print("-" * 50)
        elif money >= 300:
            print("here's the change: $%i" % (money-price))
            print("take your coffee")
            coffee -= 1
            print("coffee's quantity: %i" % coffee)
            print("-" * 50)
        elif money < 300:
            print("not enough money.")
            print("coffee's price: ", price)
            print("-" * 50)
        if not coffee:
            print("sold out. stop the sale of coffee.")
            print("-" * 50)
            break
    except:
        if x == "q":
            print("good-bye")
            break
        else:
            print("this is not number.")
            print("-" * 50)

"""
 조건에 맞지 않는 경우 무시하고 while문 계속 실행시키기 : continue
"""
# ex5. print odd number from 1 to 10
print("=" * 50)
print("ex5. print odd number from 1 to 10")
print("=" * 50)

x = 0
while x < 10:
    x += 1
    if x % 2 == 0: continue
    print(x)


"""
 Infinite loop
 
 while True: 
    수행할 문장1 
    수행할 문장2
    ...
    
 조건이나 break가 없기 떄문에 종료 할 수가 없다.
"""
# ex6. infinite loop
print("=" * 50)
print("ex6. infinite loop")
print("=" * 50)

while True:
    print("if u want to quit, ctrl+f2")