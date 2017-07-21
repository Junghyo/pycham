'''
Created on 2017. 7. 20.

@author: kitcoop
확인예제(가변 인수값 처리)
함수 정의
   receiveFoodMenu()
인수값 정의
   1번째, 어느집(중국식, 일식, 한식)
   2번째는 가변형으로 처리
    (짜장면), (짜장면, 짬뽕)

마지막으로 출력될 내용
    @@@ 집에 들리다..
    주문한 메뉴는 @@@, @@@@, @@@@ 입니다.
'''
def receiveFoodMenu(chKind, *orders):
    print(chKind,"집에 들리다!!")
    if(len(orders)>0):
        print("주문한 메뉴는 ")
        for order in orders :
            print(order, end=",")
    else :
        print("주문한 메뉴가 없습니다!!")
    print("입니다!")       

receiveFoodMenu("중국식", "짜장면", "짬뽕")    
receiveFoodMenu("한식")    
receiveFoodMenu("일식", "스시")    