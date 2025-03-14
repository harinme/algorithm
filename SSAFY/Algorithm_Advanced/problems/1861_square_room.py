import sys
sys.stdin = open('../input/1861_input.txt')
sys.setrecursionlimit(10**7)

def search(s_x, s_y):
    result = 1
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    for i in range(4):
        nx, ny = s_x + dx[i], s_y + dy[i]
        if 0 <= nx < size and 0 <= ny < size and matrix[s_x][s_y] + 1 == matrix[nx][ny]: 
            result = max(result, 1 + search(nx, ny))
    return result

t = int(input())
for tc in range(1, t+1):
    size = int(input())

    matrix = [list(map(int, input().split())) for _ in range(size)]
    cnt_matrix = [[0] * size for _ in range(size)]
    
    
    for x in range(size):
        for y in range(size):
            cnt_matrix[x][y]= search(x,y)
    
    max_count = -1
    min_num  = 0
    for i in range(size):
        for j in range(size):
            if cnt_matrix[i][j] > max_count:
                max_count = cnt_matrix[i][j]
                min_num = matrix[i][j]
            elif cnt_matrix[i][j] == max_count:
                if matrix[i][j] < min_num:
                    min_num = matrix[i][j]

    print(f'#{tc} {min_num} {max_count}')