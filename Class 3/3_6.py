a,b,c =input("세 정수를 입력하세요:").split(",")
a=int (a)
b=int (b)
c=int (c)
if a>b and a>c :
    if b<c:
        print(f"{b},{c},{a}")
    else:
        print(f"{c},{b},{a}")
elif b>a and b>c :
    if a<c:
        print(f"{a},{c},{b}")
    else:
        print(f"{c},{a},{b}")
elif c>b and c>a :
    if a<b:
        print(f"{a},{b},{c}")
    else:
        print(f"{b},{a},{c}")