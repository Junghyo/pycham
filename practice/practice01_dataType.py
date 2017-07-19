"""
Python 기본 데이터 타입
int 정수형
float 실수
bool 논리
None Null과 같은 표현
"""

int01 = int(3.5)
int02 = int("12")
print(int01)  # 3으로 반환
print(int02)  # 12로 반환
print(2e3)  # 2000.0

float01 = float(1.6425)
float02 = float("1.6124")
float03 = float("314")
print(float01)  # 1.6425
print(float02)  # 1.6124
print(float03)  # 314

float04 = float("inf")
float05 = float("-inf")
print(float04)  # 무한대
print(float05)  # -무한대

bool01 = bool(0)
bool02 = bool(12)
print(bool01)   # False. 숫자에서 0만 False
print(bool02)   # True

none01 = None
none02 = "None"
print(none01)  # None
print(none02)  # None
print(none01 is None)   # True
print(none02 is None)   # False 실제 None값이 아닌 문자열 "None"이기 때문

# 복소수
complex01 = 2+3j
print(complex01)    # 2+3j
print(complex01.real)   # 2
print(complex01.imag)   # 3
print(complex01.conjugate())    # 2-3j
print(complex01.__neg__())  # -2-3j

# 문자열
str01 = str("hihihihi")
print(str01)
print(type(str01))  # <class 'str'>
str02 = str(1123)
print(str02)
print(type(str02))  # <class 'str'>

# Octal(8진수) : 0o + 숫자
print(0o1234)   # 668

# Hexadecimal(16진수) : 0x + 숫자
print(0x1234)   # 4660
print(0xabcd)   # 43981
