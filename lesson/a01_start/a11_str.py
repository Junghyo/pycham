'''
Created on 2017. 7. 19.

@author: kitcoop
'''
str="Hardware and Shell"
str = str[:8]+" Kernel"+ str[8:]
print(str)
str = str[:15]+str[20:]
print(str)

int_val =23
float_val = 45.90876
print("int_val%3d, float_val:%0.1f"%(int_val, float_val))

data =[1,3,4]
print("최대값:{0:5<}\t최소값:{1:5>d}".format(max(data), min(data)))


print('boolean 처리:', bool(0), bool(1),\
       bool(-2), bool(3), bool(None), bool(''))

