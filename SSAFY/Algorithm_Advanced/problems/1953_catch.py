import sys
sys.stdin = open('../input/1953_input.txt')

# 터미널 구조 재구축 함수
def find_map(x, y, terminal):
    type = {
        1: [0, 1, 2, 3],  # 상, 하, 좌, 우
        2: [0, 1],       # 상, 하
        3: [2, 3],       # 좌, 우
        4: [0, 3],       # 상, 우
        5: [1, 3],       # 하, 우
        6: [1, 2],       # 하, 좌
        7: [0, 2]        # 상, 좌
    }
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    # 현재 위치의 터널 종류
    t = terminal[x][y]
    moves = []  # 이동 가능한 방향 목록

    # 해당 터널이 허용하는 기본 방향들 확인
    for d in type[t]:
        nx, ny = x + dx[d], y + dy[d]
        # 범위 내 + 인접 셀에도 터널이 있어야 함
        if 0 <= nx < x_len and 0 <= ny < y_len and terminal[nx][ny] != 0:
            # 반대 방향 매핑: 0↔1, 2↔3
            opp = {0:1, 1:0, 2:3, 3:2}[d]
            # 인접 셀의 터널이 반대 방향에서 진입 가능하면 이동 가능
            if opp in type[terminal[nx][ny]]:
                moves.append(d)

    # new_terminal[x][y]에 이동 가능한 방향들을 저장
    new_terminal[x][y] = moves
    return

# BFS로 범인을 찾는 함수
def find_suspect(terminal, hour, s_x, s_y):
    visited = [[0] * y_len for _ in range(x_len)]
    visited[s_x][s_y] = 1

    # 시작 지점 큐에 삽입 (시간은 1로 시작)
    que = [(s_x, s_y, 1)]
    count = 1  # 맨홀 위치 포함

    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]

    while que:
        x, y, t = que.pop(0)
        # t(현재 소요 시간)가 hour에 도달하면 더 이동 불가
        if t >= hour:
            continue

        # 현재 위치(terminal[x][y])에 저장된 이동 가능 방향 확인
        for d in terminal[x][y]:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < x_len and 0 <= ny < y_len and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx, ny, t + 1))
                count += 1

    return count

t = int(input())
for tc in range(1, t + 1):
    x_len, y_len, s_x, s_y, hour = map(int, input().split())
    terminal = [list(map(int, input().split())) for _ in range(x_len)]

    # 원본 터널 정보 보존 + 방향 목록을 담을 new_terminal
    new_terminal = [[[] for _ in range(y_len)] for _ in range(x_len)]

    # new_terminal 구성
    for i in range(x_len):
        for j in range(y_len):
            if terminal[i][j] != 0:
                find_map(i, j, terminal)
            else:
                new_terminal[i][j] = []

    result = find_suspect(new_terminal, hour, s_x, s_y)

    print(f'#{tc} {result}')