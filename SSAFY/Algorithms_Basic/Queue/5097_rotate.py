import sys
sys.stdin = open('5097_input.txt')

t = int(input())

for tc in range(1, t+1):
    number_total_num, try_num = map(int, input().split())
    number_list = list(map(int, input().split()))

    for _ in range(try_num):
        number_list.append(number_list.pop(0))
    
    print(f'#{tc} {number_list[0]}')