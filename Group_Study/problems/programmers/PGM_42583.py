
# 슬라이딩 윈도우 문제
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    time = 0
    current_weight = 0

    while trucks or current_weight > 0:
        # 1초 경과 → 트럭 이동
        time += 1
        out = bridge.popleft()
        current_weight -= out

        # 다음 트럭 올릴 수 있으면 올림
        if trucks and current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    return time

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10])) # 8
print(solution(100, 100, [10])) # 8