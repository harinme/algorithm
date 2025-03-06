import sys
from collections import  deque
sys.stdin = open('5102_input.txt')

t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())

    data = []
    for _ in range(E):
        data.extend(map(int, input().split()))

    S, G = map(int, input().split())

    adj_list = [[ ] for _ in range(V+1)]

    for i in range(E):
        n1, n2 = data[i * 2], data[i * 2 + 1]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    def BFS(S, G, adj_list):
        visited = [False] * (V+1)

        visited[S] = [True]
        que = deque([(S, 0)])

        while que:
            current_node, distance = que.popleft()

            if current_node == G:
                return distance

            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append((next_node, distance + 1))

        return 0

    result = BFS(S, G, adj_list)

    print(f'#{tc} {result}')