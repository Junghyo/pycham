"""
 1. 문자열
 s = '가나다'
 s = "가나다"
 여러 라인에 걸쳐 문자열을 표현하고 싶다면
 s= '''가나다
    마바사
    아자차
    '''
"""
s1 = "Hello"
print(s1)
s2 = '''
Hello.
My name is Ronaldo.
Nice to meet you.
'''
print(s2)

"""
 1.1 문자열 formatting
 format templete에 들어갈 자리를 지정해 두고 나중에 그 값을 채워 넣는 방식
 % : Formatting Operator
 ex) print("%s" % "A")
 %s 자리에 "A"가 채워짐
"""

format1 = "name: %s age: %d" % ("Yoda", 29)
print(format1)  # name: Yoda age: 29
format2 = "X = %f, Y = %10.3f" % (3.141592, 3.141592)
print(format2)
# X = 3.141592, Y =      3.142
# // 10은 전체 10자리이고 값이 적으면 앞에 빈칸을 채우게 되며 .3f는 소숫점 3자리까지만 반올림으로 반환.

"""
 %s, %d 등과 같이 대입값 형식을 지정해 주는데 이를 변환 지시어(Conversion Specifier)라 한다.

Conversion Specifier	                의미
    %s	                    문자열 (파이썬 객체를 str()을 사용하여 변환)
    %r	                    문자열 (파이썬 객체를 repr()을 사용하여 변환)
    %c	                    문자(char)
    %d 또는 %i	            정수 (int)
    %f 또는 %F	            부동소수 (float) (%f 소문자 / %F 대문자)
    %e 또는 %E	            지수형 부동소수 (소문자 / 대문자)
    %g 또는 %G	            일반형: 값에 따라 %e 혹은 %f 사용 (소문자 / 대문자)
    %o 또는 %O	            8진수 (소문자 / 대문자)
    %x 또는 %X	            16진수 (소문자 / 대문자)
    %%	                    % 퍼센트 리터럴
    
    ex)
    format3 = "%i" % "Hello" 
    print(format3)
    ERROR 발생
    TypeError: %i format: a number is required, not str
    받아들이는 지시어는 %i로 정수(int)인데 대입되는 값이 문자열이기 때문
"""

"""
 2. str(문자열 클래스)
 내부적으로 str이라는 class type. 기본적으로 unicode. 한번 설정하면 다시 변경할 수 없는 Immutable type
 index 사용 가능(0부터 시작)
"""
s3 = "Amazing Yoda"
print(s3[1])    # m
print(type(s3))     # <class 'str'>
path1 = "Hello World\nGood day"
path2 = r"Hello World\nGood day" # r을 붙이면 Escape Sequence를 표현하지 않는다.
# 또는
path3 = "Hello World\\nGood day"
print(path1)    # Hello World (enter) Good day 로 표현
print(path2)    # raw string : Hello World\nGood day
print(path3)    # \앞에 \를 더 써주면 : Hello World\nGood day

# 2.1 문자열 인덱스 활용
print("=" * 50)
print("2.1 문자열 인덱스 활용")
print("=" * 50)

ex = "Hello! Good day to die!"
print("index 1:", ex[1])    # e
print("index -1:", ex[-1])  # ! 끝에서 시작
print("index 1~5:", ex[1:5])    # ello
"""
 3. 자주 사용되는 str method
"""

# 3.1 str.join() : 문자열 결합에 사용
print("=" * 50)
print("3.1 str.join()")
print("=" * 50)

s = ["A", "B", "C", "D"]
print(s)    # ['A', 'B', 'C', 'D']
print(s[1])     # B
print(type(s))  # <class 'list'>
print(str.join(",", s))     # A,B,C,D 결합됨
print(str.join(",", s)[1])  # ,
print(type(str.join(",", s)))   # <class 'str'> 결합되서 하나의 문자열이 됨

s_join = "!!".join(s)
print(s_join)   # A!!B!!C!!D
print(type(s_join))     # <class 'str'>


# 3.2 str.split() : 특정 separator를 기준으로 문자열을 분리하여 list를 리턴
print("=" * 50)
print("3.2 str.split()")
print("=" * 50)

s = "Ronaldo@Messi@Rooney"
print(type(s))  # <class 'str'>
print(len(s))   # 20 문자열의 길이

s_split = s.split("@")
print(s_split)  # # ['Ronaldo', 'Messi', 'Rooney']
print(type(s_split))    # <class 'list'>
print(len(s_split))     # 3 list의 길이
print(str.split(s, sep="@"))    # ['Ronaldo', 'Messi', 'Rooney']


# 3.3 str.partition() : 문자열을 분리하여 앞부분(prefix), 분리자(separator), 뒷부분(suffix)
#                       등 3개의 값을 tuple로 return
print("=" * 50)
print("3.3 str.partition()")
print("=" * 50)

departure, separator, arrival = "Seattle-Seoul".partition("-")
print(departure)    # Seattle
print(separator)    # -
print(arrival)      # Seoul

player = "Ronaldo/7"
name, sep, number = player.partition("/")
print(name)  # Ronaldo
print(type(name))   # <class 'str'>
print(sep)   # /
print(number)   # 7
print(type(number))     # <class 'str'>

print(player.partition("/")) # ('Ronaldo', '/', '7')
player_p = player.partition("/")
print(player_p[0])  # Ronaldo
print(type(player_p))   # <class 'tuple'>


# 3.4 str.format()
# 위치를 기준으로 formatting : "{0}, {1}".format("A", "B") // {0}자리에 A, {1}자리에 B
print("=" * 50)
print("3.4 str.format()")
print("=" * 50)

ex1 = "{0}{1}".format("Hello!", " My friend!")
print(ex1)  # Hello! My friend!

# field명으로 formatting : "{name}, {age}".format(name="Yoda", age=28) // {name}자리에 Yoda, {age}자리에 28
ex2 = "name: {name}\nposition: {pos}\nteam: {team}".format(name="Ronaldo", pos="FW", team="Real Madrid")
print(ex2)

# object의 index 또는 key를 사용하여 formatting : x=(10, 20); 일 때, "{x[0]}, {x[1]}".format(x) // {x[0]}자리에 10, {x[1]}자리에 20
x1 = (1, 2, 3)
print(type(x1))  # (1, 2, 3) <class 'tuple'>
print(x1[1])    #2

x2 = {1, 2, 3}
print(type(x2))  # {1, 2, 3} <class 'set'>
# print(x2[1]) TypeError: 'set' object does not support indexing

x3 = [1, 2, 3]
print(type(x3))  # <class 'list'>
print(x3[1])     # 2

ex3_1 = "tuple : {x[0]} and {x[1]} and {x[2]}".format(x=x1)
print(ex3_1)

# ex3_2 = "set : {x[0]} and {x[1]} and {x[2]}".format(x=x2)
# print(ex3_2) TypeError: 'set' object does not support indexing

ex3_3 = "list : {x[0]} and {x[1]} and {x[2]}".format(x=x3)
print(ex3_3)

# 왼쪽 정렬
print("왼쪽정렬\n{0:<10}".format("hi"))

# 오른쪽 정렬
print("오른쪽정렬\n{0:>10}".format("hi"))

# 가운데 정렬
print("가운데정렬\n{0:^10}".format("hi"))

# 공백 채우기
print("공백채우기\n{0:=^10}".format("hi"))
print("공백채우기\n{0:!<10}".format("hi"))


# 3.5 str.count() : 문자 개수 세기
print("=" * 50)
print("3.5 str.count()")
print("=" * 50)

ex1 = "hasdsadaaggggggssa"
# a의 개수를 알고 싶다면
print(ex1.count("a"))   # 5


# 3.6 str.find(), str.index() : 문자 위치 알려주기(첫번째로 나오는)
print("=" * 50)
print("3.6 str.find(), str.index()")
print("=" * 50)

ex = "Hello. My name is Yoda"
print(ex.find("a"))     # 11
print(ex.index("a"))    # 11
# 차이점은 find()는 존재하지 않는 문자열을 찾으면 -1을 반환. index()는 error(ValueError: substring not found)가 뜬다.


# 3.7 str.strip() : 양쪽공백 제거(왼쪽은 lstrip, 오른쪽은 rstrip)
print("=" * 50)
print("3.7 str.strip()")
print("=" * 50)

ex = "          hi"
print(ex)   #           hi
print(ex.strip())   # hi


# 3.8 str.replace() : 문자열 바꾸기
print("=" * 50)
print("3.8 str.replace()")
print("=" * 50)

ex = "Life is too short"
print(ex.replace("too short", "too long"))


"""
 4. bytes class
 Immutable type
 문자열을 bytes로 표현하기 위해 b'문자열' 같이 접두어 b를 앞에 붙인다.
"""
text1 = "Hello"
print(type(text1))  # <class 'str'>
for b in text1:
    print(b)
# H
# e
# l
# l
# o

text2 = b"Hello"
print(type(text2))  # <class 'bytes'>

for b in text2:
    print(b)
# 72
# 101
# 108
# 108
# 111

# 문자열을 bytes들로 변경하는 인코딩을 위해 encode()를 사용.
# bytes들을 문자열로 변경하는 디코딩을 위해 decode()를 사용


text3 = b"Kill me"
print(text3)    # b'Kill me'
print(type(text3))  # <class 'bytes'>
print(text3[1])     # 105

text3_d = text3.decode("UTF-8")
print(text3_d)  # Kill me
print(type(text3_d))    # <class 'str'>
print(text3_d[1])   # i

# 문자열에 unicode를 사용하려면 \u를 사용
s1 = "A\u00e5"
print(s1)    # Aå

b = s1.encode("UTF-8")
print(b)    # b'A\xc3\xa5'

s2 = b.decode("UTF-8")
print(s2)   # Aå
