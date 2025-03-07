import sys
from pprint import pprint
sys.stdin = open('../input/snail.txt')

t = int(input())

for tc in range(1, t+1):

    size = int(input())
    snail = [[0] * size for _ in range(size)]
    pprint(snail)
        # 우, 하, 좌, 상
    dx = [0, 1, 0,-1]
    dy = [1, 0,-1, 0]

    count = 1
    x, y, dir = 0, 0, 0
    while count < size*size +1 :

            snail[x][y] = count

            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 > nx or nx >= size or 0 > ny or ny >= size or snail[nx][ny] != 0:
                dir = (dir+1) % 4
                nx = x + dx[dir]
                ny = y + dy[dir]

            x, y = nx, ny
            count += 1


    # print 방법 꼭 이해하고 넘어가기
    print(f'#{tc}')
    for row in snail:
        print(*row)