import sys
sys.stdin = open('4835_input.txt')

def bus_test(start, bus, charge):
    charge_count = 0

    while True:
        move = charge
        if start + move >= len(bus):
            return charge_count
        for i in range(start+charge, start, -1):
            if bus[i] == -1:
                return charge_count
            elif bus[i] == charge:
                charge_count += 1
                start = i
                break
            move -=1
            if move == 0:
                return 0

    

T = int(input())

for tc in range(1,T+1):
    charge, end, charge_stop_num = map(int, input().split())
    charge_stop_list = list(map(int, input().split()))

    bus = [0] * (end +1)
    bus[-1] = -1 # 종점 도착 판별을 위해서
    bus[0] = charge 
    for i in charge_stop_list:
        bus[i] = charge
    result = bus_test(0, bus, charge)
    
    print(f'#{tc} {bus} {result}')