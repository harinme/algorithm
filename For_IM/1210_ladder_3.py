import sys
sys.stdin = open('ladder1.txt')

t = 10
for _ in range(10):
    tc = int(input())
    size = 100
    ladder = [list(map(int, input().split())) for _ in range(size)]

    # 시작 인덱스 (99, 2인 곳의 인덱스)
    x = size - 1
    for i in range(size):
        if ladder[x][i] == 2:
            y = i

    def go(x, y, ladder):
        while True:
            #     좌, 우, 상
            dx = [ 0, 0,-1]
            dy = [-1, 1, 0]

            ladder[x][y] = 0
            pre_x, pre_y = x, y

            for i in range(len(dx)-1):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < size and 0 <= ny < size and ladder[nx][ny] == 1:
                    x, y = nx, ny
                else:
                    continue
            if y == pre_y:
                x, y = x + dx[2], y + dy[2]
            if x == 0:
                return y

    result = go(x, y, ladder)

    print(f'#{tc} {result}')