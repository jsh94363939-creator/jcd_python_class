for i in range(2,13):
    a=i/2
    b=i/3
    c=i/5
    d=i/7
    e=i/11
    if a==1 or b==1 or c==1 or d==1 or e==1:
        print(f"{i} : 소수")
    else :
        print(f"{i} : 합성수")