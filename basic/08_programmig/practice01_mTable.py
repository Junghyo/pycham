'''
Created on 2017-07-24 20:22

@ product name : PyCharm Community Edition

@ author : yoda
'''

# 구구단

def mTable1(x):
    result = []
    for i in range(1, 10):
        result.append(x * i)
    return result

print(mTable1(2))



def mTable2(x):
    result = []
    i = 1
    while i < 10:
        result.append(x * i)
        i += 1
    return result

print(mTable2(3))

for x in range(2, 10):
    print("{0}단".format(x))
    for y in range(1, 10):
        print(x * y, " ",  end='')
    print('')