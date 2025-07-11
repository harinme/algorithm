import sys
from collections import deque
# from pprint import pprint

# sys.stdin = open('test.txt')
input = sys.stdin.readline

# 2) "?" 바로 위까지 내려가는 시뮬레이션
def simulate_down(start_order):
    state = start_order[:]  # 깊은 복사
    # 1행부터 target_line-1행까지
    for r in range(1, target_line):
        for j in range(player - 1):
            # ladder[r][2*j+1] 가 1이면 가로선 존재 → swap
            if ladder[r][2*j+1] == 1:
                state[j], state[j+1] = state[j+1], state[j]
    return state

# 3) "?" 바로 아래부터 위로 올라가는 역시뮬레이션
def simulate_up(final_order):
    state = final_order[:]  # 깊은 복사
    # ladder_line행부터 target_line+1행까지 역순
    for r in range(ladder_line, target_line, -1):
        for j in range(player - 1):
            if ladder[r][2*j+1] == 1:
                state[j], state[j+1] = state[j+1], state[j]
    return state

# 4) 두 상태를 비교해 "?" 행(char 리스트) 생성
def build_missing_row(top_state, bottom_state):
    res = ['*'] * (player - 1)
    i = 0
    while i < player - 1:
        # 4-1) 그대로 같으면 '*'
        if top_state[i] == bottom_state[i]:
            i += 1
        # 4-2) 한 칸 옆으로 swap 해야 일치한다면 '-'
        elif (i + 1 < player and
              top_state[i] == bottom_state[i+1] and
              top_state[i+1] == bottom_state[i]):
            res[i] = '-'
            # 다음 비교를 위해 top_state에도 swap 반영
            top_state[i], top_state[i+1] = top_state[i+1], top_state[i]
            i += 2
        # 4-3) 그 외는 불가능 → 모두 'x'
        else:
            return ['x'] * (player - 1)
    return res

player = int(input().rstrip())
start = [chr(ord('A') + i) for i in range(player)]
ladder_line = int(input().rstrip())

goal = list(input().strip())

# print(goal)
ladder = [[] for _ in range(ladder_line+1)]

for i in range(player):
    if i == player-1:

        ladder[0].append(1)
    else:
        ladder[0].extend([1,0])


target_line = -1
# print(ladder)
for i in range(1, ladder_line + 1):
    line = deque(input().strip())

    for j in range(player):
        # 10번째 라면(세로줄 정보만 넣어야 하기에)
        if j == player -1 :
            ladder[i].append(1)
        else:
            line_elem = line.popleft()
            if line_elem == '*':
                # (세로줄, 가로줄 연결 정보)
                ladder[i].extend([1, 0])
            elif line_elem == '-':
                ladder[i].extend([1 ,1])
            else: # ? 라면
                target_line = i
                ladder[i].extend([1, -1])

# pprint(ladder)


'''
사다리 타기 결과를 구하는 함수를 구현(따라가면 어디가 나오는지)
??? 기준 위는 위에서 아래로 갔을 때의 좌표
??? 기준 아래는 아래에서 위로 갔을 때의 좌표

각 좌표 값의 차이를 ??? 표에서 동일하게 바꿔주기 위해 ???를 구하는 함수 구현
'''
top_state = simulate_down(start)
bottom_state = simulate_up(goal)
missing_row = build_missing_row(top_state, bottom_state)

# 결과 출력
print(''.join(missing_row))