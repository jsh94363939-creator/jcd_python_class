a,b=input("점의 좌표 x,y를 입력하시오 :").split()
a=int(a)
b=int(b)
if (((a**2)-3)+((b**2)-3))**0.5 <=5:
    print(f"원의 내부에 있음")
else :
    print(f"원의 외부에 있음")