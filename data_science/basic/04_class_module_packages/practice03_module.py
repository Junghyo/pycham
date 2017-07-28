'''
Created on 2017-07-21 15:57

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 myModules
 
 from 모듈명 import 함수명
 import 모듈1[, 모듈2[,... 모듈N]
"""

from data_science.basic.myModules import mod2

"""
 if __name__ == "__main__": 의 의미
 
 만약 myModules 파일에서 test를 위해 출력을 한 다음
 작업 파일에서 해당 module을 import를 하여 출력을 한다면
 moudle 파일에서 출력한 결과가 같이 나와버린다.
 이를 막기 위해 myModules 파일에서 출력code(print) 위에
 if __name__ == "__main__": 를 선언하면 작업 파일에서는
  module의 출력결과가 나오지 않는다.
"""
print(mod2.pi)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.pi, 4.4))

import sys
print(sys.path) # python library가 설치된 directory를 보여줌
sys.path.append("C:/pycharm/basic/myModules")