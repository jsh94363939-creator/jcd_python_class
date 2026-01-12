a,b=input("점의 좌표 x,y를 입력하세요:").split()
a=int(a)
b=int(b)
if a>0 and b>0:
    print("1사분면")
elif a>0 and b<0:
    print("4사분면")
elif a<0 and b>0:
    print("2사분면")
elif a<0 and b<0:
    print("3사분면")
else:
    print(f"{a},{b}")