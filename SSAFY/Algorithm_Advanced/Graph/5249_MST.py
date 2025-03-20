import sys
import heapq
sys.stdin = open('./input/5249.txt')

def prim_mst(edges_list, V, start_node=0):

    # 정점의 개수는 0번 인덱스도 포함
    visited = [False] * (V + 1)
    que = []

    visited[start_node] = True
    for next_node, cost in edges_list[start_node]:
        # 노드 번호가 아닌 cost 기준으로 우선 순위를 주고 싶기 때문에 cost, next_node 순으로 넣음
        heapq.heappush(que, (cost, next_node))

    mst_cost = 0
    edges_used = 0

    # 점점의 개수는 V+1개 이므로 간선의 수가 V개가 되기 전까지 돌려야함.
    while que and edges_used < V:
        cost, node = heapq.heappop(que)

        if visited[node]:
            continue
        
        visited[node] = True
        mst_cost += cost
        edges_used += 1
        
        for next_node, cost in edges_list[node]:
            if not visited[next_node]:
                heapq.heappush(que, (cost, next_node))
    
    return mst_cost

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())

    edges_list = [[]  for _ in range(V+1)]

    # 인접 리스트 생성
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges_list[s].append((e, w))
        edges_list[e].append((s, w))

    # 가중치가 낮은 순서대로 인접 리스트 정렬
    # for i in edges_list:
    #     i.sort(key= lambda x: x[1])
    # print(edges_list)

    result = prim_mst(edges_list, V)


    print(f'#{tc} {result}')