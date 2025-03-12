import sys
sys.stdin = open('../input/5188_input.txt')

def min_sum(matrix):
    n = len(matrix)
    cost = [[float('inf')] * n for _ in range(n)]
    cost[0][0] = matrix[0][0]
    
    # 하, 우 방향 이동
    dx = [1, 0]
    dy = [0, 1]
    
    q = []
    q.append((0, 0))
    
    while q:
        x, y = q.pop(0)
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if cost[nx][ny] > cost[x][y] + matrix[nx][ny]:
                    cost[nx][ny] = cost[x][y] + matrix[nx][ny]
                    q.append((nx, ny))
    
    return cost[n-1][n-1]

# 테스트 코드
t = int(input())
for tc in range(1, t+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result = min_sum(matrix)
    print(f'#{tc} {result}')