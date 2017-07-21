'''
Created on 2017. 7. 21.

@author: kitcoop
'''
from a04_callpackage import a02_weekendplan as week
print("##주말계획1##")
for p in week.plan():
    print(p,end="\n")


from a04_callpackage.a02_weekendplan import *
print("##주말계획2##")
for p in plan():
    print(p,end="\n")