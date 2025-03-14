import sys
sys.stdin = open('../input/1486_input.txt')

def min_number(cur_height):
    global min_height
    if cur_height >= height:
        if cur_height < min_height:
            min_height = cur_height
        return

    for i in range(human_num):
        if used[i]:
            continue
        used[i] = True
        min_number(cur_height + human_list[i])
        used[i] = False

t = int(input())
for tc in range(1, t+1):
    human_num, height = map(int, input().split())
    human_list = list(map(int, input().split()))

    path = []
    used = [False] * human_num
    min_height = sum(human_list)
    

    min_number(0)
    result= min_height - height

    print(f'#{tc} {result}')