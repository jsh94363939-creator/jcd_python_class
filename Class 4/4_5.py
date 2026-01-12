print(f"맛나 식당에 오신 것을 환영합니다.메뉴는 다음과 같습니다 \n- 햄버거(입력 b)\n- 치킨(입력 c)\n- 피자(입력 p)")
number=input('메뉴를 선택하세요(알바텟 b, c, p 입력) :')
print(number)
while 1:
    if number== b or number== c or number== p:
        if number==b:
            print("햄버거를 선택하였습니다")
            break
        elif number==c:
            print("치킨를 선택하였습니다")
            break
        else:
            print("피자를 선택하였습니다")
            break        
    else :
        number=input("메뉴를 다시 입력하세요(알바텟 b, c, p 입력) :")