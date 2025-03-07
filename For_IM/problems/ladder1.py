import sys
sys.stdin = open('../input/ladder1.txt')

test_case = 10
for _ in range(test_case):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for idx in range(len(ladder)):
        if ladder[-1][idx] == 2:
            start_idx = idx


      #  좌, 우, 상
    dx = [0, 0,-1]
    dy = [-1, 1, 0]

    def ladder_game(y, x = 99):
        while x > 0:
            ### !!!!! 이미 이동한 칸도 1이기 때문에 지나간 표시를 안 해주면 무한 반복문에 빠진다
            ladder[x][y]= 0
            pre_x, pre_y = x, y
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < len(ladder) and ladder[nx][ny] == 1:
                    x, y = nx, ny
                    continue
            if (pre_x, pre_y) == (x, y):
                x += dx[2]
            if x == 0:
                return y
    result = ladder_game(start_idx)
    print(f'#{tc} {result}')