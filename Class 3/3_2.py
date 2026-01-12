name=input("이름를 입력하세요 :")
height=int(input("키를 입력하세요(단위 cm) :"))
if height < 140:
    print(f"{name} 님은 놀이기구를 탈 수 없습니다")
else :
    print(f"{name} 님은 놀이기구를 탈 수 있습니다")
