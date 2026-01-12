b=0
number=int(input("1에서 9까지의 수를 입력하세요 :"))
while b==0:
    if number>=1 and number<=9:
        for i in range(1,10):
            a=number*i
            print(f"{number} * {i} = {a}")
        b=1
    else :
        number=int(input("1에서 9까지의 수를 다시 입력하세요 :"))