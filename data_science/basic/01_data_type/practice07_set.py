"""
 set
 unique elements로만 구성된 집합. { } 사용. 순서에 의존하는 기능을 사용할 수 없다.
 Unordered, index 사용 불가
 set = {element1, element2, ...., elementn}

"""
# how to make set ?
s1 = {1, 2, 3}
print(s1)  # {1, 2, 3}
print(type(s1))  # <class 'set'>
# s2 = set("a", "b",  "c", "d")
# print(s2)     TypeError: set expected at most 1 arguments, got 4

s2 = set([1, 2, 3])
print(s2)  # {1, 2, 3}

s3 = set("Hello")
print(s3)  # {'H', 'l', 'e', 'o'} unique elements, unordered
# 이런 기능으로 종종 자료형의 중복을 ㅔ거하기 위해 사용되기도 한다.
t1 = tuple("11214235211")
print(t1)  # ('1', '1', '2', '1', '4', '2', '3', '5', '2', '1', '1')
print(set(t1))  # {'1', '5', '3', '2', '4'} set으로 중복 제거
print(tuple(set(t1)))  # ('1', '4', '3', '2', '5') 중복 제거 후 다시 tuple 변환

"""
 1. intersection, union, difference 구하기
"""
# 1-1. intersection, &
print("=" * 50)
print("1-1. intersection, &")
print("=" * 50)
s1 = set([1, 2, 3, 4, 5, 10])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = set([1, 2, 3])
s4 = set([1, 5])
# & 사용
print(s1 & s2)  # {4, 5}
print(s2 & s3)  # set() : 교집합이 없는 경우
print(s1 & s2 & s4)     # {5} 2개 이상도 가능
# intersection()
print(s1.intersection(s2))  # {4, 5}
print(s2.intersection(s1))  # {4, 5}
print(s2.intersection(s3))  # set()
print(s2.intersection(s1).intersection(s4))  # {5}
print(s2.intersection(s1.intersection(s4)))  # {5}
# 1-2. union, |
print("=" * 50)
print("1-2. union, |")
print("=" * 50)

ex1 = set("abcdef")
ex2 = set([1, 2, 3, 4, 5])
ex3 = set([1, 2, 6])

# | 사용
print(ex1 | ex2)  # {1, 2, 3, 'b', 4, 5, 'e', 'c', 'f', 'd', 'a'}
print(ex1 | ex2 | ex3)  # {1, 2, 3, 4, 5, 6, 'b', 'a', 'c', 'e', 'd', 'f'}
# 2개 이상도 가능. 중복된 data는 하나만 표시된다.

# union()
print(ex1.union(ex3))   # {1, 2, 6, 'f', 'b', 'd', 'c', 'e', 'a'}
print(ex2.union(ex3.union(ex1)))    # {1, 2, 3, 4, 5, 6, 'b', 'e', 'd', 'f', 'a', 'c'}
print(ex1.union(ex2).union(ex3))    # {1, 2, 3, 4, 5, 6, 'd', 'f', 'b', 'e', 'a', 'c'}


# 1-3. difference, -
print("=" * 50)
print("1-3. difference, -")
print("=" * 50)

ex1 = set("abcde")
ex2 = set("defgh")
ex3 = set([1, 2, 3, 4, 5, 6])
ex4 = set([3, 4, 7, 8])
ex5 = set([1, 5, 3, 9, 10])

# - 사용
print(ex1 - ex2)    # {'b', 'c', 'a'}
print(ex3 - ex4)    # {1, 2, 5, 6}
print(ex3 - ex4 - ex5)  # {2, 6}

# difference 사용
print(ex3.difference(ex4))  # {1, 2, 5, 6}
print(ex3.difference(ex4).difference(ex5))  # {2, 6}


"""
 2. set 관련 method
"""
# 2-1. set.add() : 값 1개 추가하기
print("=" * 50)
print("2-1. set.add()")
print("=" * 50)

s1 = set([1, 2, 3])
print(s1)   # {1, 2, 3}
set.add(s1, 4)
print(s1)   # {1, 2, 3, 4}
s1.add(5)
print(s1)   # {1, 2, 3, 4, 5}


# 2-2. set.update() : 값 여러개 추가하기
print("=" * 50)
print("2-2. set.update()")
print("=" * 50)

s1 = set([1, 2, 3])
print(s1)   # {1, 2, 3}
set.update(s1, "abc")
print(s1)   # {'a', 1, 2, 3, 'b', 'c'}
s1.update([5, 6, "d", "e", "f"])
print(s1)   # {1, 2, 3, 5, 6, 'f', 'a', 'd', 'b', 'c', 'e'}

# 2-3. set.remove(), set.discard() : 특정값 제거하기
print("=" * 50)
print("2-3. set.remove(), set.discard()")
print("=" * 50)

s1 = set([1, 2, 3, "a", "b"])
print(s1)   # {1, 2, 'a', 3, 'b'}
set.discard(s1, "a")
print(s1)   # {1, 2, 3, 'b'}
s1.discard(1)
print(s1)   # {2, 3, 'b'}
set.remove(s1, "b")
print(s1)   # {2, 3}
s1.remove(3)
print(s1)   # {2}

# 2-4. set.clear() : 모두 삭제
print("=" * 50)
print("2-4. set.clear()")
print("=" * 50)

s1 = set([1, 2, 3])
print(s1)   # {1, 2, 3}
s1.clear()
print(s1)   # set()