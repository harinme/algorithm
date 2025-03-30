import sys
sys.stdin = open('./input/5251.txt')

import heapq
def dijkstra(s_node):
    que = []
    distance = [float('inf') for _ in range(V)]
    distance[s_node] = 0
    heapq.heappush(que, (0, s_node))

    while que:
        cost, c_node = heapq.heappop(que)
        if c_node == last_node:
            return distance[c_node]
        
        for n_node, move_cost in adj_list[c_node]:
            new_cost = move_cost + cost
            if new_cost < distance[n_node]:
                distance[n_node] = new_cost
                heapq.heappush(que, (new_cost, n_node))



t = int(input())
for tc in range(1, t+1):
    last_node, E = map(int, input().split())
    V = last_node + 1
    adj_list = [[ ] for _ in range(V)]
    
    for _ in range(E):
        s, e, w= map(int, input().split())
        adj_list[s].append((e, w))
    
    result = dijkstra(0)

    print(f'#{tc} {result}')
    