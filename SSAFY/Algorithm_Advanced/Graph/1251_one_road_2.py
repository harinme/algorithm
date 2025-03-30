import sys
import heapq
sys.stdin = open('./input/1251.txt')

def prim():
    pass

def make_edges(cnt, start):
    if cnt == 2:
        
        return
    
    for i in range(start, island_num):
        if used[i] == True:
            continue
        used[i] = True
        path.append(island_list[i], i+1)
        make_edges(cnt+1)

        used[i] = False
        path.pop()


t = int(input())
for tc in range(1, t+1):
    island_num = int(input())
    island_list = [[ ] for _ in range(island_num)]
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    for i in range(island_num):
        island_list[i] = x_list[i], y_list[i]

    print(island_list)
    path = []
    used = [False] * island_num
        
    

    print(f'#{tc} ')