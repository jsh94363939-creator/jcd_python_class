b=0
a=int(input("숫자를 입력하세요 :"))
for i in range(1,a+1):
    b+= (1/i)**2
print(f"결과는 {b}")