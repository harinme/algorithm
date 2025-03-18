import sys
sys.stdin = open('./input/5208.txt')

def bus(data, start_idx, end, count):
    global min_count
    # 가지치기
    if count >= min_count:
        return
    charge = data[start_idx]
    if start_idx+1<= end < start_idx + charge+1:
        # 도착했는데 이때 카운트가 최소 카운트보다 작았다면, 값 갱신
        if count < min_count:
            min_count = count
            return
        # 현재 충전 지점부터 다음에 갈 수 있는 지점까지 체크
    for idx in range(start_idx + 1, start_idx + charge+1):
        bus(data, idx, end, count+1)
    

t = int(input())
for tc in range(1, t+1):
    bus_stop_num, *data = map(int, input().split())
    
    # 버스의 인덱스를 버스 정류장 번호 그 자체로 하기 위해서 제일 처음에 0 삽입
    bus_list = [0]
    bus_list.extend(data)
    
    # 가장 많은 충전 횟수는 1번 이후부터 나오는 모든 충전소에서 충전을 한 경우,
    # 1번 정류장은 충전 횟수로 안 치고, 도착 지점도 충전 안 하기 때문에 -2
    min_count = bus_stop_num - 2
    
    bus(bus_list, 1, bus_stop_num, 0)

    print(f'#{tc} {min_count}')