'''
Created on 2017-07-21 16:28

@ product name : PyCharm Community Edition

@ author : yoda
'''
def sum(a, b):
    return a+b

def safe_sum(a, b):
    if type(a) != type(b):
        print("type is different. can't add")
        return
    else:
        result = sum(a, b)
    return result

if __name__ == "__main__":
    print("-" * 50)
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))