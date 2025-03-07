import sys
sys.stdin = open('../input/9490_pang.txt')

def pang(x, y, matrix, n, m):
    num = matrix[x][y]
    pang_sum = matrix[x][y]

    #     상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    for i in range(len(dx)):
        for j in range(1, num + 1):
            nx = x + (dx[i] * j)
            ny = y + (dy[i] * j)
            if 0 <= nx < n and 0 <= ny < m:
                pang_sum += matrix[nx][ny]
    return pang_sum

t = int(input())
for tc in range(1, t + 1):
    # m개씩 n줄
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    pang_num = [[0 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):

            pang_num[x][y] += pang(x, y, matrix, n, m)

    max_pang = float('-inf')

    for i in pang_num:
        for j in i:
            if j > max_pang:
                max_pang = j

    print(f'#{tc} {max_pang}')