import sys
sys.stdin = open('../input/BFS.txt')

V, E = map(int, input().split())

data = list(map(int, input().split()))

adj_list = [[ ] for _ in range(V+1)]

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# print(adj_list)

def BFS(adj_list, start):
    visited = [False] * (V+1)
    que = [start]
    visited[start] = True

    while que:
        current_node = que.pop(0)
        print(f'-{current_node}', end='')

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)

BFS(adj_list, 1)