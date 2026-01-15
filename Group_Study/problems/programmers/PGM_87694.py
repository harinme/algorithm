from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102
    
    matrix = [[0] * MAX for _ in range(MAX)]

    # 1. 모든 직사각형 내부를 1로 채움
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2, y2*2+1):
            for x in range(x1*2, x2*2+1):
                matrix[y][x] = 1

    # 2. 내부는 2로 표시 (외곽선과 구분)
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1*2+1, y2*2):
            for x in range(x1*2+1, x2*2):
                if matrix[y][x] == 1:
                    matrix[y][x] = 2

    # matrix에서 1인 곳만 외곽선
    
    s_r, s_c = characterY * 2, characterX * 2
    g_r, g_c = itemY * 2, itemX * 2
 
    visited = [[False] * MAX for _ in range(MAX)]
    que = deque()
    que.append((s_r, s_c, 0))
    visited[s_r][s_c] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while que:
        r, c, step = que.popleft()
        if r == g_r and c == g_c:
            return step // 2
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < MAX and 0 <= nc < MAX and not visited[nr][nc] and matrix[nr][nc] == 1:
                visited[nr][nc] = True
                que.append((nr, nc, step + 1))

    return -1  # 도달 불가능

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))