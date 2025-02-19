import sys
sys.stdin = open('sum.txt')


def cross_sum(num, matrix, size):
    # 대각선
    # 하-우,하-좌
    dx = [1, 1]
    dy = [1, -1]
    if num == 0:  # 하-우
        x, y = 0, 0
    else:  # 하-좌
        x, y = 0, 99

    cross_sum = 0
    for _ in range(size):
        cross_sum += matrix[x][y]
        nx = x + dx[num]
        ny = y + dy[num]
        x, y = nx, ny
    return cross_sum

# 테스트 케이스
t = 10
for _ in range(t):
    tc = int(input())
    size = 100
    # 100 * 100 배열
    matrix = [list(map(int, input().split())) for _ in range(size)]

    # 행의 최고값 max_row
    max_row = float('-inf')
    for i in matrix:
        if sum(i) > max_row:
            max_row = sum(i)
    # 렬의 최고값 max_col
    max_col = float('-inf')
    for y in range(size):
        sum_col = 0
        for x in range(size):
            sum_col += matrix[x][y]
        if sum_col > max_col:
            max_col = sum_col

    max_cross= max(cross_sum(0,matrix,size), cross_sum(1,matrix,size))
    result = max(max_cross, max_col, max_row)

    print(f'#{tc} {result}')