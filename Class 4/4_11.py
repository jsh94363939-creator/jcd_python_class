a=0
b=0
while 1:
    b+=1
    a+=7
    print(f"day:{b}     달팽이의 위치:{a}미터")
    if a>30:
        print(f"\n우물을 탈출하는데 걸린 날은 {b}일입니다.")
        break
    else :
        a-=5