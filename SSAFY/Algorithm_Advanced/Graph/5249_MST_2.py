import sys
import heapq
sys.stdin = open('./input/5249.txt')

def mst(s_node):
    total = 0
    edges = 0
    # 0 1 2 (2)
    visited =[False] * (V+1)
    visited[s_node] = True
    que = []
    for e_n, cost in adj_list[s_node]:
        heapq.heappush(que, (cost, e_n))
 


    while que and edges < V:
        cost, cur_n = heapq.heappop(que)

        if visited[cur_n] == True:
            continue

        visited[cur_n] = True
        total += cost
        edges += 1

        for next_n, next_cost in adj_list[cur_n]:
            if visited[next_n] == False:
                heapq.heappush(que, (next_cost, next_n))
    return total

t= int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    # 노드는 0~ v번까지 v+1개
    adj_list = [[ ] for _ in range(V+1)]
   
    for i in range(E):
        s_n, e_n, cost = map(int, input().split())
        adj_list[s_n].append((e_n, cost))
        adj_list[e_n].append((s_n, cost))
   
    result = mst(0)

    print(f'#{tc} {result}')