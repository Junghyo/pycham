print("HELLO WORLD")
print("안녕하세요")
import os
print(os.getcwd())

# 그래프 그리기
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel("some numbers")
plt.show()

sum=0
for cnt in range(1,11):
    sum+=cnt
    print("countdown", cnt)
print(sum)

x=100
if(x>0):
    print("x의 값:",x,"\nx는 0보다 큽니다.")
else:
    print("x의 값:",x,"\nx는 0 이하입니다.")