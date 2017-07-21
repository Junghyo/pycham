'''
Created on 2017. 7. 20.
확인예제
1. 장바구니에 물건을 5개를 담은 카트를 list로 
만들고, 중복을 제거한 후, 다시 list의 내용을 
확인하세요..
물건명 :  사과, 바나나, 딸기, 바나나, 오렌지
2. 일정계획을 두사람이 세웠다.
A 사람이 세운 계획 (set)
B 사람이 세운 계획 (set)
의 내용을 
1) 중복된 계획
2) 중복을 제거된 계획
   을 list로 전체 계획을 나타내고,
3) 그 중에서 마지막 계획을 나타내세요

@author: kitcoop
'''
cartList = ["사과","바나나","딸기","바나나","오렌지"]
print("초기 장바구니 리스트:",cartList)
setCart =set(cartList)
cartList = list(setCart)
print("중복 제거된 장바구니 리스트",cartList)
plan01={"휴식","잠","학습","식사"}
plan02={"산책","잠","학습","식사","영화관람"}
print("전체 중복된 계획", plan01.intersection(plan02))
plan03 = list(plan01.union(plan02))
print("전체 중복제거된 게획",plan03)
print("마지막 계획:",plan03[ len(plan03)-1] )





