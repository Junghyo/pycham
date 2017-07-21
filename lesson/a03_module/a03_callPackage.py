'''
Created on 2017. 7. 21.

@author: kitcoop
'''
from a04_callpackage import a01_calculator as ca
result = ca.plus(10, 30)
print("결과:{0}".format(result))
result = ca.minus(10, 30)
print("결과:{0}".format(result))
'''
확인예제..
a04_callpackage에서
 a02_weekendplan.py
     plan함수를 선언
        return 주말계획리스트..
a04_packageExp.py
   a02_weekendplan의 plan함수를 호출 해서 출력..
'''




