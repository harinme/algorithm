import sys
sys.stdin = open('./input/5249.txt')

def kruskal_mst(edges_list, V):
    
    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    mst_cost = 0

    for w, s, e in edges_list:
        if find_set(parent, s) != find_set(parent, e):
            union(parent, rank, s, e)
            mst_cost += w

    return mst_cost
    

def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def union(parent, rank, x , y):
    root_x, root_y = find_set(parent, x), find_set(parent, y)

    if root_x == root_y:
        return
    
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1



t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())

    edges_list = []

    # 인접 리스트 생성
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges_list.append((w, s, e))

    # print(edges_list)
    edges_list.sort(key= lambda x: x[0])
    # 가중치가 낮은 순서대로 인접 리스트 정렬

    result = kruskal_mst(edges_list, V)


    print(f'#{tc} {result}')