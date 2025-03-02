import sys
sys.stdin = open('5102_input.txt')

t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())
    data = []
    for _ in range(E):
        data.extend(map(int, input().split()))
    
    start, end = map(int, input().split())

    adj_list = [[ ] for _ in range(V+1)]

    for i in range(E):
        n1 = data[i * 2]
        n2 = data[i * 2 + 1]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1) 

    visited = [0] * (V+1)
    visited[start] = 1
    que =[]
    que.append((0, start))
    
    while que:
        num, curent_node = que.pop(0)
        if curent_node == end:
            break

        num +=1
        for next_node in adj_list[curent_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                que.append((num, next_node))

    if curent_node !=end:
        num = 0

    print(f'#{tc} {num}')