# snail.py
# 아래에 코드를 작성하시오.
def snail(goal, up, down) :
    days = 0
    rest = goal
    # 예외처리
    if rest == 0 : return 0
    
    while(True) :
        print(rest)
        rest -= up
        days += 1
        if(rest <0) :
            break
        rest += down
    
    return days

print(snail(100, 5, 2))
print(snail(0,5,1))