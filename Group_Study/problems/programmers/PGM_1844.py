from collections import deque
def solution(maps):
    start = (0,0,1)
    n = len(maps)
    m = len(maps[0])
    g_x, g_y = n-1, m-1
    visited = [[False] * m  for _ in range(n)]
    road = 1
    visited[0][0] = True

    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def bfs(start):
        
        que = deque()
        que.append(start)
        while que:

            x, y, step = que.popleft()
            if x == g_x and y == g_y:
                return step
            

            for dx, dy in dir:
                nx = x+dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == road and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    que.append((nx, ny, step +1))
        
        return -1


    answer = bfs(start)


    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))