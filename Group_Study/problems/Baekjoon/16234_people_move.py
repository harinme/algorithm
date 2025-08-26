import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def check(x, y, lands, visited):
    if visited[x][y]:
        return []
    
    union = [(x, y)]
    sum_union = lands[x][y]
    visited[x][y] = True
    
    # BFS를 위한 큐 (리스트로 구현)
    queue = [(x, y)]
    
    while queue:
        cx, cy = queue.pop(0)  # 첫 번째 요소 제거 (큐 방식)
        
        for i in range(4):
            dx, dy = cx + dir[i][0], cy + dir[i][1]
            if 0 <= dx < ground and 0 <= dy < ground and not visited[dx][dy]:
                if min_p <= abs(lands[dx][dy] - lands[cx][cy]) <= max_p:
                    visited[dx][dy] = True
                    union.append((dx, dy))
                    sum_union += lands[dx][dy]
                    queue.append((dx, dy))
    
    if len(union) > 1:  # 연합이 형성되었으면
        len_union = len(union)
        union_p = sum_union // len_union
        
        for i in range(len_union-1, -1, -1):
            ux, uy = union.pop()
            lands[ux][uy] = union_p
        
        return True  # 인구이동 발생
    
    return False

ground, min_p, max_p = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(ground)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

days = 0

while True:
    visited = [[False] * ground for _ in range(ground)]
    moved = False
    
    for i in range(ground):
        for j in range(ground):
            if check(i, j, lands, visited):
                moved = True
    
    if not moved:
        break
    
    days += 1

print(days)