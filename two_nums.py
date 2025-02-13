import sys
sys.stdin = open('two_nums.txt')

def arr_mult(short, long):
    max_sum = float('-inf')
    for i in range(len(long) - len(short) + 1):
        sum_list = [0] * len(short)
        for j in range(len(short)):
            sum_list[j] = short[j] * long[i+j]
        mult_sum = sum(sum_list)
        if mult_sum > max_sum:
            max_sum = mult_sum
    return max_sum



t= int(input())
for tc in range(1, t+1):
    a_num, b_num = map(int, input().split())
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))

    if a_num > b_num:
        result = arr_mult(b_nums, a_nums)
    else:
        result = arr_mult(a_nums, b_nums)

    print(f'#{tc} {result}')
