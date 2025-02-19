import sys
sys.stdin = open('switch.txt')

def wrong_switch(s_num ,s_staus, s_goal):
    for idx in range(s_num):
        if s_staus[idx] != s_goal[idx]:
            return idx
    return False
        

def switch(s_num, switch_staus, start_num):
    for idx in range(start_num, s_num):
        switch_staus[idx] = 1 - switch_staus[idx]
    return switch_staus



t = int(input())

for tc in range(1, t + 1):
    s_num = int(input())
    s_staus = list(map(int, input().split()))
    s_goal = list(map(int, input().split()))
    count = 0
    while True:
        if s_staus == s_goal:
            break
        wrong_idx = wrong_switch(s_num, s_staus, s_goal)
        switch(s_num, s_staus, wrong_idx)
        count +=1


    print(f'#{tc} {count}')