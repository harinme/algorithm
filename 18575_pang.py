import sys
sys.stdin = open('18575_pang.txt')

def pang_game(pang, pang_num, size, x, y):
    #    상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    pang_num[x][y] = pang[x][y]
    for i in range(1, size):
        for j in range(len(dx)):
            nx = x + dx[j] * i
            ny = y + dy[j] * i

            if 0 <= nx < size and 0 <= ny < size:
                pang_num[x][y] += pang[nx][ny]

t = int(input())
for tc in range(1, t+1):
    size = int(input())
    pang = [list(map(int, input().split())) for _ in range(size)]

    pang_num = [[0]*size for _ in range(size)]


    for x in range(size):
        for y in range(size):
            pang_game(pang, pang_num, size, x, y)

    max_pang = float('-inf')
    min_pang = float('inf')
    for i in pang_num:
        for j in i:
            if j > max_pang:
                max_pang = j
            if j < min_pang:
                min_pang = j

    result = max_pang - min_pang

    print(f'#{tc} {result}')