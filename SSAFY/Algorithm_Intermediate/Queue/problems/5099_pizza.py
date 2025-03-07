from collections import deque
import sys

sys.stdin = open('../input/5099_input.txt')
t = int(input())

for tc in range(1, t + 1):
    oven_size, pizza_num = map(int, input().split())
    pizza_cheese = list(map(int, input().split()))

    oven = deque()
    count = 0

    for _ in range(oven_size):
        count += 1
        oven.append((count, pizza_cheese.pop(0)))  # (피자번호, 치즈양)

    # 오븐에 피자가 1개만 남을 때까지 진행
    while len(oven) > 1:
        num, cheese = oven.popleft()  # 활성 슬롯(왼쪽)에서 피자 꺼내기
        cheese //= 2  # 치즈 녹이기

        if cheese > 0:
            # 치즈가 남으면 같은 슬롯에 재삽입한 후, 회전(-1)해서 다음 슬롯 활성화
            oven.appendleft((num, cheese))
            if len(oven) > 1:
                oven.rotate(-1)
        else:
            # 치즈가 다 녹았다면, 대기 중인 새 피자가 있다면 교체
            if pizza_cheese:
                print('----------')
                count += 1
                oven.append((count, pizza_cheese.pop(0)))
                print(oven)

    # 최종 남은 피자의 번호 출력
    print(f'#{tc} {oven[0][0]}')



