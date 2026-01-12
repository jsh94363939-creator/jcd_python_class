a,b,c=input("세개 복권번호를 입력하시오:").split()
a=int(a)
b=int(b)
c=int(c)
if a==2 or b==2 or c==2:
    if a==3 or b==3 or c==3:
        if a==9 or b==9 or c==9:
            print("상금 1억원")
    elif a==9 or b==9 or c==9:
        print("상금 1천만원")
    else:
        print("상금 1만원")
elif a==3 or b==3 or c==3:
    if a==2 or b==2 or c==2:
        if a==9 or b==9 or c==9:
            print("상금 1억원")
    elif a==9 or b==9 or c==9:
        print("상금 1천만원")
    else:
        print("상금 1만원")
elif a==9 or b==9 or c==9:
    if a==3 or b==3 or c==3:
        if a==2 or b==2 or c==2:
            print("상금 1억원")
    elif a==2 or b==2 or c==2:
        print("상금 1천만원")
    else:
        print("상금 1만원")
else:
    print("다음 기회에...")
    