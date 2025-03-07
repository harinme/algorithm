import sys
sys.stdin = open('../input/2001_kill_fly_2.txt')

# 파리채 영역 내 파리 수 구하는 함수
def kill_fly(s_x, s_y, tool_size, matrix):
    fly_sum = 0
    for i in range(tool_size):
        for j in range(tool_size):
            fly_sum += matrix[s_x + i][s_y + j]
    return fly_sum


t = int(input())
for tc in range(1, t+1):
    matrix_size, tool_size = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(matrix_size)]
    fly_num = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    for x in range(matrix_size - tool_size + 1):
        for y in range(matrix_size - tool_size + 1):
            fly_num[x][y] = kill_fly(x, y, tool_size, fly)

    max_num = float('-inf')
    for i in fly_num:
        for j in i:
            if j > max_num:
                max_num = j

    print(f'#{tc} {max_num}')