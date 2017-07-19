"""
 # list
 동적배열(Dynamic Array)
 list 안의 요소(element)들은 그 값을 자유롭게 변경할 수 있는 Mutable type
"""
# how to make list?
# list = [element1, element2, ...., elementn]
ex1 = [1, 2, 3, 4, 5]
ex2 = []
print(ex1)  # [1, 2, 3, 4, 5]
print(ex2)  # []
print("list length:", len(ex1))  # list length: 5
print("list type:", type(ex2))  # list type: <class 'list'>

"""
 1. list's indexing and slicing
"""
# 1-1. list's indexing
print("=" * 50)
print("1-1. list's indexing")
print("=" * 50)

ex = [1, 2, 3]
print("list ex:", ex)   # [1, 2, 3]
print("ex's index 1:", ex[1])   # 2
print("index0 + index2:", ex[0]+ex[2])  # 4
print("index-1:", ex[-1])   # 3

# list 안에 또 list 넣기
ex1 = [1, 2, 3]
ex2 = ["a", "b", "c", ex1]
print(ex1)
print(ex2)  # ['a', 'b', 'c', [1, 2, 3]]
print(ex2[-1])  # [1, 2, 3]
print(ex2[3])   # [1, 2, 3]
# ex2에서 ex1의 2를 선택하려면?
print(ex2[-1][1])   # 2
print(ex2[3][1])    # 2

# 3중 list
ex3 = [1, 2, ["a", "b", ["Ronaldo", "Messi"]]]
print(ex3)  # [1, 2, ['a', 'b', ['Ronaldo', 'Messi']]]
print(ex3[2])   # ['a', 'b', ['Ronaldo', 'Messi']]
# b 선택하기
print(ex3[2][1])    # b
# Ronaldo 선택하기
print(ex3[2][2][0])     # Ronaldo

# 1-2. list's slicing
print("=" * 50)
print("1-2. list's slicing")
print("=" * 50)

a = [1, 2, 3, 4, 5]
print(a[0:2])   # index0<= a < index2 : index0, index1만 선택. [1, 2]
print(a[:4])    # [1, 2, 3, 4]
print(a[1:])    # [2, 3, 4, 5]

# 중첩된 list의 slicing
a = [1, 2, 3, ["a", "b", "c"], 4, 5]
# a~b만 나타내고 싶다
print(a[3][0:2])    # ['a', 'b']


"""
 2. list's operator
"""
# 2-1. list plus(+)
print("=" * 50)
print("2-1. list plus(+)")
print("=" * 50)

a = [1, 2, 3]
b = ["a", "b"]
print(a+b)  # [1, 2, 3, 'a', 'b']

# 2-2. list's repeat(*)
print("=" * 50)
print("2-2. list's repeat(*)")
print("=" * 50)

print(a*3)  # 3번 반복 : [1, 2, 3, 1, 2, 3, 1, 2, 3]

a = [1, 2, 3]
b = "hi"
# print(a+b) TypeError: can only concatenate list (not "str") to list
print(a+list(b))    # [1, 2, 3, 'h', 'i']

"""
 3. 리스트의 수정, 변경과 삭제(revise, change, delete)
"""
print("=" * 50)
print("3. list : revise, change, delete")
print("=" * 50)

a = [1, 2, 3]
# 수정하기
# 2번째를 4로 바꾸고 싶다
a[1] = 4
print(a)    # [1, 4, 3]

a = [1, 2, 3, 4]
# 2, 3을 a, b, c, d로 바꾸고 싶다.
a[1:3] = ["a", "b", "c", "d"]
print(a)    # [1, 'a', 'b', 'c', 'd', 4]

a = [1, 2, 3]
# 2를 e, f로 바꾸고 싶다
a[1] = ["e", "f"]
print(a)    # [1, ['e', 'f'], 3] 이렇게 나와버린다.

b = [1, 2, 3]
b[1:2] = ["e", "f"]
print(b)    # [1, 'e', 'f', 3] 이렇게 범위를 지정해주어야 제대로 수정되어 나온다.

# 삭제하기
# []을 이용
a = [1, 2, 3, 4, 5]
# 3을 지우고 싶다.
a[2:3] = []
print(a)    #

a = [1, 2, 3, 4, 5]
# 2, 3, 4를 지우고 싶다.
a[1:4] = []
print(a)    # [1, 5]

# del 이용 : del 객체
a = [1, 2, 3, 4, 5]
# 4를 지우고 싶다.
del a[3]
print(a)    # [1, 2, 3, 5]

a = [1, 2, 3, 4, 5]
# 3,4 를 지우고 싶다.
del a[2:4]
print(a)    # [1, 2, 5]

"""
 4. 리스트 관련 함수들
"""
# 4-1. append() : list 맨 마지막에 element 새로 추가
print("=" * 50)
print("4-1. append()")
print("=" * 50)

a = [1, 2, 3]
# 4 추가
a.append(4)
print(a)    # [1, 2, 3, 4]

# a 추가
a.append("a")
print(a)    # 1, 2, 3, 4, 'a']

# a,b 추가(요소 2개)
# a.append("a", "b")
# print(a) TypeError: append() takes exactly one argument (2 given). 오직 요소 하나만 가능

# list안에 list 및 다른 자료형도 추가할 수 있다.
# list ["a", "b"] 추가
a.append(["a", "b"])
print(a)    # [1, 2, 3, 4, 'a', ['a', 'b']]


# 4-2. sort() : list 정렬
print("=" * 50)
print("4-2. sort()")
print("=" * 50)

a = [10, 1, 3, 7, 4, 9, 2, 6, 8]
# 숫자 정렬
a.sort()
print(a)    # [1, 2, 3, 4, 6, 7, 8, 9, 10]

# 문자 정렬
a = ["나", "히", "라", "모", "사"]
a.sort()
print(a)    # ['나', '라', '모', '사', '히'] 한글도 가능


# 4-3. reverse() : list 뒤집기(역정렬이 아닌 단순 뒤집기)
print("=" * 50)
print("4-3. reverse()")
print("=" * 50)

a = ["Life", "is", "cool"]
a.reverse()
print(a)    # ['cool', 'is', 'Life']


# 4-4. index() : 위치 반환
print("=" * 50)
print("4-4. index()")
print("=" * 50)
a = ["a", "b", "c"]
print(a.index("b"))  # 1


# 4-5. insert() : list에 element 삽입(원하는 위치에)
print("=" * 50)
print("4-5. insert()")
print("=" * 50)

a = [1, 2, 3]
a.insert(0, 4)
print(a)    # [4, 1, 2, 3]
a. insert(3, "a")
print(a)    # [4, 1, 2, 'a', 3]
a.insert(3, [1, 2])
print(a)    # [4, 1, 2, [1, 2], 'a', 3] 자료형도 추가 가능

# 4-6. remove() : list에서 요소 제거
print("=" * 50)
print("4-6. remove()")
print("=" * 50)

a = [1, 2, 3, 4, 3, 3]
a.remove(3)
print(a)    # [1, 2, 4, 3, 3] 첫번째 3이 지워짐
a.remove(3)
print(a)    # [1, 2, 4, 3] 두번쨰 3이 지워짐


# 4-7. count() : 해당하는 element의 개수 세기
print("=" * 50)
print("4-7. count()")
print("=" * 50)

a = [1, 2, 3, 1, 1, 5, 1]
print(a.count(1))   # 4


# 4-8. extend() : 리스트 확장. list만 들어올 수 있다.
print("=" * 50)
print("4-8. extend()")
print("=" * 50)

a = [1, 2, 3]
a.extend([4, 5])
print(a)  # [1, 2, 3, 4, 5]

b = [1, 2, 3]
print(b + [4, 5])   # [1, 2, 3, 4, 5]
