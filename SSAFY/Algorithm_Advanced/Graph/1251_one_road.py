import sys
import heapq
sys.stdin = open('./input/1251.txt')

def prim_mst(edges_list, island_num, start_node=0):

    visited = [False] * (island_num)
    que = []

    visited[start_node] = True
    for next_node, cost in edges_list[start_node]:
        heapq.heappush(que, (cost, next_node))

    mst_cost = 0
    edges_used = 0 

    while que and edges_used < island_num - 1:
        cost, node = heapq.heappop(que)

        if visited[node] == True:
            continue
        
        visited[node] = True
        mst_cost += cost
        edges_used += 1

        for next_node, cost in edges_list[node]:
            if not visited[next_node]:
                heapq.heappush(que, (cost, next_node))

    return mst_cost


def recur(cnt, start):
    if cnt == 2:
        x1, y1= path[0][0]
        idx1 = path[0][1]
        x2, y2 = path[1][0]
        idx2 = path[1][1]
        x = x1 - x2
        y = y1 - y2
        x_y = x**2 + y**2
        cost = round(x_y * E)
        edges_list[idx1].append((idx2, cost))
        edges_list[idx2].append((idx1, cost))
        return
    
    for i in range(start, island_num):
        if visited[i] == True:
            continue
        visited[i] = True
        path.append((island_list[i], i))
        recur(cnt + 1, i)
        visited[i] = False
        path.pop()




t = int(input())
for tc in range(1, t+1):
    island_num = int(input())
    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))
    E = float(input())
    
    island_list = []
    for i in range(island_num):
        island_list.append((islands_x[i], islands_y[i]))

    path = []
    visited = [False] * island_num

    data = []
    edges_list = [[]  for _ in range(island_num)]
    recur(0, 0)
    result = prim_mst(edges_list, island_num)

    print(f'#{tc} {result}')
