'''
Created on 2017. 7. 19.

@author: kitcoop
'''
print("### 주말의 일정계획")
schList =["06:00 기상","06:30 운동","09:00 도서관에서","12:00 친구와 식사",]

print("기본일정",schList)
schList.insert(1,"6:15 일정계획 점검")
print("2번째 일정 추가:",schList)
schList.remove("12:00 친구와 식사")
print("일정 취소  친구와 식사",schList)
schList.extend(["16:00 산책","18:00 영화관람"])
print("일정 추가(2개) 후,",schList)
print("09:00 도서관에서 index:", schList.index("09:00 도서관에서" ))