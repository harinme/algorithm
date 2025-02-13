import sys
sys.stdin = open('kill_fly.txt')

t = int(input())
for tc in range(1, t+1):
    size, tool_size = map(int, input().split())

    flys = [list(map(int, input().split())) for _ in range(size)]

    max_count = float('-inf')
    dy = [ 0, 1]

    for x in range(size - tool_size + 1):
        for y in range(size - tool_size + 1):
            count = 0
            for i in range(tool_size):
                nx = x + i
                for j in range(tool_size):
                    ny = y + j*dy[1]
                    count += flys[nx][ny]
            if count > max_count:
                max_count = count




    print(f'#{tc} {max_count}')