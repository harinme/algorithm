import sys
sys.stdin = open('../input/20551_input.txt')

def candy(candy_1, candy_2, candy_3):
    result = 0
    # 각 상자에 최소 사탕 개수 조건 검사 (첫 번째: ≥1, 두 번째: ≥2, 세 번째: ≥3)
    if candy_1 < 1 or candy_2 < 2 or candy_3 < 3:
        return -1
    # 이미 조건 만족: candy_1 < candy_2 < candy_3이면 0 반환
    if candy_1 < candy_2 < candy_3:
        return result
    
    # 조건 만족할 때까지 반복적으로 사탕을 줄임
    while not (candy_1 < candy_2 < candy_3):
        # 두 번째 상자가 세 번째 상자보다 크거나 같으면, 두 번째 상자에서 사탕을 1개 먹음
        if candy_2 >= candy_3:
            if candy_2 <= 1:  # 최소 조건을 벗어나면 불가능
                return -1
            candy_2 -= 1
            result += 1
        # 그렇지 않고, 첫 번째 상자가 두 번째 상자보다 크거나 같으면, 첫 번째 상자에서 사탕을 1개 먹음
        elif candy_1 >= candy_2:
            if candy_1 <= 1:
                return -1
            candy_1 -= 1
            result += 1
        # 안전 체크: 만약 어느 상자라도 1개 미만이면 불가능
        if candy_1 < 1 or candy_2 < 1 or candy_3 < 1:
            return -1
    return result

t = int(input())
for tc in range(1, t+1):
    candy_1, candy_2, candy_3 = map(int, input().split())
    result = candy(candy_1, candy_2, candy_3)
    print(f'#{tc} {result}')
