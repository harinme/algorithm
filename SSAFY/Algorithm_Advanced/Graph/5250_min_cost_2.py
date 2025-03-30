import sys
sys.stdin = open('./input/5250.txt')


import heapq

def bfs():
    s_x, s_y = 0, 0
    matrix_cost = [[float('Inf') for _ in range(size)] for _ in range(size)]
    matrix_cost[s_x][s_y]= 0
      #  상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    

    que = []
    heapq.heappush(que, (0, s_x,s_y))

    while que:
        cost, cur_x, cur_y = heapq.heappop(que)
        if cur_x == size-1 and cur_y == size-1:
            return matrix_cost[cur_x][cur_y]
        
        for i in range(len(dx)):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                diff = matrix[nx][ny] - matrix[cur_x][cur_y]
                move_cost = 1 + max(0, diff)
                new_cost = cost + move_cost

                if new_cost < matrix_cost[nx][ny]:
                    matrix_cost[nx][ny] = new_cost
                    heapq.heappush(que, (new_cost, nx, ny))

    return matrix_cost[size-1][size-1]


t= int(input())
for tc in range(1, t+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result =  bfs()

    print(f'#{tc} {result}')