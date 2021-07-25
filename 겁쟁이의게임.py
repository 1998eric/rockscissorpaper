import random


def rsp(a,b):
    if(a==b):
        print("비겼습니다")
    elif(a=="가위"):
        if(b=="바위"):
            print("님 짐")
        if(b=="보"):
            print("이겼읍니다.")
    elif(a=="바위"):
        if(b=="보"):
            print("님 짐")
        if(b=="가위"):
            print("이겼읍니다.")        
    elif(a=="보"):
        if(b=="가위"):
            print("님 짐")
        if(b=="바위"):
            print("이겼읍니다.")

            

while True:
    a = input("가위, 바위, 보중에 선택하시오: ")
    b_rand = random.randrange(0,3)

    
    if b_rand == 0: b="가위"
    elif b_rand == 1: b="바위"
    elif b_rand == 2: b="보"

    rsp(a,b)
    print("당신은:", a," 상대는: ", b)
