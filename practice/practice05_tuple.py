"""
 tuple
 list와 다른 점 : 새로운 element를 추가하거나 갱신, 삭제하는 일을 할 수 없다.
 Immutable type
 tuple = (element1, element2, ...., elementn)
"""

# how to make tuple?
t1 = ()
t2 = (1, )
t3 = (1)
t4 = (1, 2, 3)
t5 = 1, 2, 3
t6 = ("a", "b", ("cd", "ef"))
print(t1)   # ()
print(t2)   # (1,)
print(t3)   # 1
print(t4)   # (1, 2, 3)
print(t5)   # (1, 2, 3)
print(t6)   # ('a', 'b', ('cd', 'ef'))
print(type(t3))     # <class 'int'> 하나만 집어넣으면 반드시 뒤에 , 가 붙어야 한다.

# indexing & slicing
t1 = (1, 2, "a", "b")
print(t1[1])    # 2
print(t1[:2])   # (1, 2)
print(t1[2:])   # ('a', 'b')

# tuple plus(+)
t1 = (1, 2, 3)
print(t1 + (4, 3))    # (1, 2, 3, 4, 3)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 3, 4)
print(t1 + tuple("a"))  # (1, 2, 3, 'a')
# print(t1 + tuple(3)) TypeError: 'int' object is not iterable

# tuple multiple(*)

t1 = (1, 2, 3)
print(t1 * 3)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# tuple에 variable 할당
name = ("Cristiano", "Ronaldo")
print(name)  # ('Cristiano', 'Ronaldo')

# 변수 할당 : firstname, lastname
firstname, lastname = name
print(lastname, "", firstname)