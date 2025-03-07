import sys

sys.stdin = open('../input/num_sort.txt')

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(n - 1):
        min_num = i
        for j in range(i+1, n):
            if num_list[min_num] > num_list[j]:
                min_num = j
        num_list[min_num], num_list[i] = num_list[i], num_list[min_num] 

    print(f'#{test_case} {num_list}')
