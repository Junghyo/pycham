'''
Created on 2017. 7. 19.

@author: kitcoop
'''
names=["톰","제임스","찰스"]
tom=[90,85,70]
james=[99,77,66]
charls=[100,100,100]
points=[tom,james,charls]
print("이름\t", "총점\t","평균")
for idx in range( 0, len(names)):
    print(names[idx],"\t", sum(points[idx]),"\t",format(sum(points[idx])/3,"3.1f"))
