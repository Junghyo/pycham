'''
Created on 2017. 7. 19.

@author: kitcoop
'''
print("## 구구단 출력 ##")
for start in range(2,10) :
    print("      {0}단".format(start,"4s"))
    for end in range(1,10) :
        if end==3:
            continue;
        if start==8 and end==5:
            break;
        print(start, " X ", end," = ", format(start*end,"2d") )
    if start==8:
         break;     