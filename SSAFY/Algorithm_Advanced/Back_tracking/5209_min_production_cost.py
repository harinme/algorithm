import sys
sys.stdin = open('./input/5209.txt')

def choice_factory(cnt, cost):
    global min_cost
    if cost >= min_cost:
        return
    if cnt == product_num:
        if cost < min_cost:
            min_cost = cost
        return
    
    for i in range(len(factory)):
        if visited_factory[i] == True:
            continue
        for j in range(product_num):
            if visited[j] == True:
                continue
            visited[j] = True
            visited_factory[i] = True
            choice_factory(cnt+1, cost+factory[i][j])
            visited[j] = False
            visited_factory[i] = False
            


t = int(input())
for tc in range(1, t+1):
    product_num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(product_num)]
    visited = [False] * product_num
    visited_factory = [False] * product_num
    factory = list(zip(*matrix))

    min_cost = float('inf')

    choice_factory(0, 0)

    print(f'#{tc} {min_cost}')