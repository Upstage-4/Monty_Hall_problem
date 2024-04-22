from random import randint

n = int(input("반복횟수 입력 : "))

def montyhall(n):
    normal_win_cnt = 0
    normal_lose_cnt = 0
    change_win_cnt = 0
    change_lose_cnt = 0
    
    for i in range(n):
        reward = randint(1, 3)
        answer = randint(1, 3)
        
        val = randint(1, 3)
        
        while(reward == val or answer == val):
            val = randint(1, 3)

        if(reward == answer) :
            normal_win_cnt += 1
        else :
            normal_lose_cnt += 1
        
    print(f'normal_win_cnt : {normal_win_cnt}')
    print(f'normal_lose_cnt : {normal_lose_cnt}')
    normal_rate = normal_win_cnt*100/(normal_win_cnt + normal_lose_cnt)
    print(f'normal rate : {normal_rate}%')

montyhall(n)
