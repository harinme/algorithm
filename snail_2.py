import sys
sys.stdin = open('snail_2.txt')

T = int(input())

for test_case in range(1, T + 1):
    size = int(input())
    
    # [수정 전] 기존 코드에서는 각 셀을 [0] (리스트)로 초기화했음.
    # matrix = [[[0] for _ in range(size)] for _ in range(size)]
    #
    # [수정 후] 숫자 채우기를 위해 각 셀을 0으로 초기화합니다.
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    # [수정 전] 기존에는 상, 하, 좌, 우 순서로 방향 배열이 작성되어 있었음.
    # dx = [-1, 1, 0, 0]
    # dy = [ 0, 0,-1, 1]
    #
    # [수정 후] 일반적인 나선형 문제에서는 오른쪽, 아래, 왼쪽, 위 순서로 진행합니다.
    dx = [0, 1, 0, -1]  # x 방향 이동: 오른쪽(0), 아래(1), 왼쪽(0), 위(-1)
    dy = [1, 0, -1, 0]  # y 방향 이동: 오른쪽(1), 아래(0), 왼쪽(-1), 위(0)
    
    x, y = 0, 0  # 시작 좌표
    direction = 0  # 초기 방향: 오른쪽 (인덱스 0)
    
    # [수정 전] 기존 코드는 이중 for문과 내부에서 별도의 나선형 채우기를 시도했으나,
    # 전체 행렬을 한 번에 나선형으로 채우려면 전체 이동 횟수를 size*size로 잡아야 함.
    #
    # [수정 후] 1부터 size*size까지 순서대로 채워나갑니다.
    for num in range(1, size * size + 1):
        matrix[x][y] = num  # 현재 위치에 숫자 채우기
        
        # 다음 좌표 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # [수정 전] 조건문에서 matrix[nx][ny] != 0로 되어 있었음.
        # 하지만 문제 조건은 "범위를 벗어나거나 이미 숫자가 채워졌다면 방향 전환"이므로,
        # 채워지지 않은 경우(값이 0)만 이동해야 함.
        #
        # [수정 후] 다음 좌표가 범위를 벗어나거나 이미 채워져 있으면 방향 전환.
        if nx < 0 or nx >= size or ny < 0 or ny >= size or matrix[nx][ny] != 0:
            # [수정 전] 기존 코드에서는 방향 전환 시 (dir + 1) % 3으로 되어 있었으나,
            # 4방향이므로 % 4를 사용해야 합니다.
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        # [수정 전] 이동에 성공했을 때 현재 좌표를 업데이트하지 않았음.
        # [수정 후] 올바른 좌표로 이동하기 위해 업데이트합니다.
        x, y = nx, ny
    
    # 결과 출력
    print(f'#{test_case}')
    for row in matrix:
        print(' '.join(map(str, row)))