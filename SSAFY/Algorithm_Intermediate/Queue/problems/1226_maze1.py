import sys
sys.stdin = open('../input/1226_input.txt')

def maze_test(s, maze, size, visited):
    que =[]
    que.append(s)
    visited[s[0]][s[1]] = True
        # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    while que:
        x, y = que.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if maze[nx][ny] == 3:
                    return 1
                if maze[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return 0

t = 10
for _ in range(10):
    tc = int(input())
    size = 16
    maze = [list(map(int, input().strip())) for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]
    s= (1, 1)


    result = maze_test(s, maze, size, visited)

    
    print(f'#{tc} {result}')
   