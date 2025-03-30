import sys
sys.stdin = open('./input/5248.txt')

def find_parent(node):
    if parents[node] != node:
        parents[node] = find_parent(parents[node])
    return parents[node]

def union(a, b):
    root_a , root_b = find_parent(a), find_parent(b)

    if root_a == root_b:
        return
    
    if rank[a] > rank[b]:
        parents[root_b] = root_a
    elif rank[a] == rank[b]:
        parents[root_b] = root_a
        rank[a] += 1
    else:
        parents[root_a] = root_b
    return


t = int(input())
for tc in range(1, t+1):
    s_num, request_num = map(int, input().split())

    data = list(map(int, input().split()))
    
    parents = [i for i in range(s_num+1)]
    rank = [0] * (s_num+1)
    for i in range(request_num):
        n1,  n2= data[i*2], data[i*2 + 1]
        union(n1, n2)

    for i in range(1, s_num+1):
        find_parent(i)

    parents = set(parents)
    print(f'#{tc} {len(parents)-1}')