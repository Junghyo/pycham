"""
 Dictionary (dict)
 키(Key) - 값(Value)" 쌍을 요소로 갖는 collection.(like Java map)
 key : Immutable type
 value : Immutable, Mutable type(possible)
 dict = {key1: value1, key2: value2, ....., keyn: valuen}

 생성시 key 중복은 자제한다.

"""

# how to make dict?
ex = {"name": "Ronaldo", "age": 32, "loc": "portugal"}
print(ex)   # {'name': 'Ronaldo', 'age': 32, 'loc': 'portugal'}
# name의 value를 알고 싶다.
print(ex["name"])   # Ronaldo
# print(ex[1]) KeyError: 1. list, tuple 처럼 index 사용 불가
print(ex["age"])    # 32

# key에 정수값도 가능
ex = {1: "ronaldo", 2: "messi", 3: "rooney"}
print(ex[2])    # messi

# value에 자료형 data도 넣을 수 있다.
ex = {"a": [1, 2, 3], "b": (4, 5), "c": {"name": "ronaldo"}}
print(ex["a"])  # [1, 2, 3]             <class 'list'>
print(ex["b"])  # (4, 5)                <class 'tuple'>
print(ex["c"])  # {'name': 'ronaldo'}   <class 'dict'>
print(ex["c"]["name"])  # ronaldo

# 1. 딕셔너리 쌍 추가, 삭제하기
# 쌍 추가하기(순서 상관없이 추가됨) dict[key] = value
ex = {1: "a"}
print(ex)   # {1: 'a'}
ex[2] = "b"
print(ex)   # {1: 'a', 2: 'b'}
ex["nation"] = "korea"
print(ex)   # {1: 'a', 2: 'b', 'nation': 'korea'}
ex["data"] = [1, 2, 3]
print(ex)   # {1: 'a', 2: 'b', 'nation': 'korea', 'data': [1, 2, 3]} 자료형도 추가 가능

# value 수정하기 dict[key] = 수정할 value
ex[1] = "abc"
print(ex)   # {1: 'abc', 2: 'b', 'nation': 'korea', 'data': [1, 2, 3]}

# 요소 삭제하기 : del dict[key]
del ex[1]
print(ex)   # {2: 'b', 'nation': 'korea', 'data': [1, 2, 3]} # key값 1이 삭제
del ex["data"]
print(ex)   # {2: 'b', 'nation': 'korea'} key값 data가 삭제

# key값에 무엇을 넣을 수 있을까?
ex[(1, 2)] = "abc"  # tuple은 immutable이라 key값으로 설정 가능
# ex[[1, 4]] = "def" TypeError: unhashable type: 'list' list는 mutable(가변)이라 안된다. key는 반드시 immutable
print(ex)

# 2. dict 관련 method
# 2-1. dict.keys() : key list 만들기
print("=" * 50)
print("2-1. dict.key()")
print("=" * 50)

a = {"name": "ronaldo", "phone": "01012341234", "team": "real madrid"}
print(a.keys())      # dict_keys(['name', 'phone', 'team'])
a_key = list(a.keys())
print(a_key)         # ['name', 'phone', 'team']
print(dict.keys(a))  # dict_keys(['name', 'phone', 'team'])

# dict.keys()  using for loop
for k in a.keys():
    print(k)
# name
# phone
# team



# 2-2. dict.values() : value list 만들기
print("=" * 50)
print("2-2. dict.values()")
print("=" * 50)

print(a.values())       # dict_values(['ronaldo', '01012341234', 'real madrid'])
print(dict.values(a))   # dict_values(['ronaldo', '01012341234', 'real madrid'])
a_value = list(a.values())
print(a_value)          # ['ronaldo', '01012341234', 'real madrid']

# set 변환
a_set = set(a.values())
print(a_set)    # (('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid'))
# list 변환
a_list = list(a.values())
print(a_list)   # ['ronaldo', '01012341234', 'real madrid']
# tuple 변환
a_tuple = tuple(a.values())
print(a_tuple)  # ('ronaldo', '01012341234', 'real madrid')

# dict.values() using for loop
for v in a.values():
    print(v)
# ronaldo
# 01012341234
# real madrid

for i in a.keys():
    print(a[i])


# 2-3. dict.items() : key, value 쌍으로 얻기
print("=" * 50)
print("2-3. dict.items()")
print("=" * 50)

print(a.items())        # dict_items([('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid')])
print(dict.items(a))    # dict_items([('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid')])
a_items = list(a.items())
print(a_items)          # [('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid')]

print(a_items[1])           # ('phone', '01012341234')
print(type(a_items[1]))     # <class 'tuple'>

# set 변환
a_set = set(a.items())
print(a_set)    # {('team', 'real madrid'), ('phone', '01012341234'), ('name', 'ronaldo')}
# list 변환
a_list = list(a.items())
print(a_list)   # [('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid')]
# tuple 변환
a_tuple = tuple(a.items())
print(a_tuple)  # (('name', 'ronaldo'), ('phone', '01012341234'), ('team', 'real madrid'))

# dict.items() using for loop
for i in a.items():
    print(i)
    print(list(i))
    print(tuple(i))
    print(set(i))


# 2-4. dict.clear() : key, value 전부 지우기
print("=" * 50)
print("2-4. dict.clear()")
print("=" * 50)

a.clear()
print(a)    # {}
print(a.clear())    # None


# 2-5. dict.get() : key에 해당하는 value값을 출력
print("=" * 50)
print("2-5. dict.get()")
print("=" * 50)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get("name"))    # pey
print(a["name"])        # pey
print(dict.get(a, "phone", "novalue"))  # 0119993323
print(dict.get(a, "age", "nokey"))  # 해당하는 key가 없으면 default로 "nokey" 반환
print(a.get("team", "해당 키가 없습니다"))  # 해당 키가 없습니다


# 2-6. dict.update() : dict안의 여러 data를 한꺼번에 갱신
print("=" * 50)
print("2-6. dict.update()")
print("=" * 50)

people = [('kim', 30), ("lee", 40)]
mydict = dict(people)   # dict형으로 변환
a.update(mydict)
print(a)    # {'name': 'pey', 'phone': '0119993323', 'birth': '1118', 'kim': 30, 'lee': 40}
print(a["kim"])     # 30
# 한꺼번에 update할 수 있다.


# 2-7. 해당 key가 dict에 있는지 조사하기 : key값 in dict
print("=" * 50)
print("2-7. 해당 key가 dict에 있는지 조사하기")
print("=" * 50)

# using in
print("name" in a)  # true
print("abc" in a)  # false
