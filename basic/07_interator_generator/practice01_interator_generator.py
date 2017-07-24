'''
Created on 2017-07-24 19:22

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 iterator
 list, Set, Dictionary와 같은 컬렉션이나 문자열과 같은 문자 Sequence 등은
 for 문을 써서 하나씩 데이타를 처리할 수 있는데,
 이렇게 하나 하나 처리할 수 있는 컬렉션이나 Sequence 들을
 Iterable 객체(Iterable Object)라 부른다.
 
 iter() : "iter(Iterable객체)" 와 같이 사용하여 그 Iterable 객체의 iterator를 return
 
 Iterable 객체에서 실제 Iteration을 실행하는 것은 iterator로서,
 iterator는 next 메서드를 사용하여 다음 요소(element)를 가져온다.
 만약 더이상 next 요소가 없으면 StopIteration Exception을 발생시킨다.
 
"""

mylist = list(range(1, 3))
it = iter(mylist)
print(it)   # <list_iterator object at 0x000000000222B438>
print(type(it)) # <class 'list_iterator'>
print(next(it))
print(next(it))
# print(next(it)) # StopIteration error


"""
 어떤 클래스를 Iterable 하게 하려면,
 그 클래스의 iterator를 리턴하는 __iter__() 메서드를 작성해야 한다.
 어떠한 경우든 Iterator가 되는 클래스는
 __next()__ 메서드 (Python 2 인 경우 next() 메서드) 를 구현해야 한다.
 실제 for 루프에 Iterable Object를 사용하면,
 해당 Iterable의 __iter__() 메서드를 호출하여 iterator를 가져온 후
 그 iterator의 next() 메서드를 호출하여 루프를 돌게 된다.
"""


class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n


coll = MyCollection()
for x in coll:
    print(x)



"""
 generator
 
 Generator 함수(Generator function)는 함수 안에 yield 를 사용하여
 데이타를 하나씩 리턴하는 함수이다.
 
 Generator 함수가 처음 호출되면,
 그 함수 실행 중 처음으로 만나는 yield 에서 값을 리턴한다.
 Generator 함수가 다시 호출되면
 직전에 실행되었던 yield 문 다음부터 다음 yield 문을 만날 때까지 문장들을 실행하게 된다.
 이러한 Generator 함수를 변수에 할당하면 그 변수는 generator 클래스 객체가 된다.
"""

# generator method

def generator():
    yield 1
    yield 2
    yield 3
    yield 15

# generator object
g = generator()
print(type(g))  # <class 'generator'>

# next()
n = next(g); print(n)
n = next(g); print(n)
n = next(g); print(n)
# n = next(g); print(n) # StopIteration

for x in generator():
    print(x)


"""
 generator expression
 
 List Comprehension은 앞뒤를 [...] 처럼 대괄호로 표현한다면,
 Generator Expression (...) 처럼 둥근 괄호를 사용한다. 
 Generator Expression은 List Comprehension과 달리
 실제 리스트 컬렉션 데이타 전체를 리턴하지 않고,
 그 표현식만을 갖는 Generator 객체만 리턴한다.
 즉 실제 실행은 하지 않고,
 표현식만 가지며 위의 yield 방식으로 Lazy Operation을 수행하는 것이다.
"""

print("=" * 50)

# generator expression
g = (n * n for n in range(1001))
print(type(g))  # <class 'generator'>

# print(list(g)) # list 변환

# 10개 출력
for i in range(10):
    value = next(g)
    print(value)

# 나머지 출력
for x in g:
    print(x)
