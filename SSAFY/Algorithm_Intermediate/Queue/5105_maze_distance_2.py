import sys
from pprint import pprint
sys.stdin = open('5105_input.txt')

t = int(input())

def maze_test(s, maze_size, e, maze):
    visited_matrix = [[False] *maze_size  for _ in range(maze_size)]
    que= []
    que.append(s)
    visited_matrix[s[0]][s[1]] = True

        # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    while que:
        x, y, num= que.pop(0)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < maze_size and 0 <= ny < maze_size:
                if maze[nx][ny] == 0 and visited_matrix[nx][ny] == False:
                    # 직접 num을 수정하면 오류가 발생할 수 있음
                    # num += 1
                    visited_matrix[nx][ny] = True
                    que.append((nx, ny, num+1))
                elif maze[nx][ny] == 3:
                    return num
        
    return 0

for tc in range(1, t+1):
    maze_size = int(input())
    maze = [list(map(int, input().strip())) for _ in range(maze_size)]

    e, s = [], []

    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 3:
                e = (i, j)
            if maze[i][j] == 2:
                s = (i, j, 0)

    result = maze_test(s, maze_size, e, maze)

    print(f'#{tc} {result}')