import sys
sys.stdin = open('./input/5247.txt')

t = int(input())
for tc in range(1, t+1):
    num, target_num = map(int, input().split())
    count = 0

    while num != target_num:
        if num > target_num:
            while num - target_num >= 10:
                num -= 10
                count += 1
            num -= 1
            count += 1
        else: # num이 더 작은 수 라면?
            while num*2 <= target_num:
                num*=2
                count += 1
            num +=1
            count += 1

    print(f'#{tc} {count}')