import sys
# input = sys.stdin.readline
sys.stdin = open('test.txt')

def binary_serch(target, result, left, right):
    if left > right:
        return 0
    if result == 1:
        return 1
    if left == right:
        if card_list[left] == target:
            return 1
        else:
            return 0

    mid = (left + right) // 2
    if card_list[mid] == target:
        return 1
    elif card_list[mid] < target :
        return(binary_serch(target, result, mid + 1, right))
    else:
        return(binary_serch(target, result, left, mid -1))


card_num = int(input().rstrip())
# -10,000,000 <= card_num <= 10,000,000
card_list = list(map(int, input().split()))
card_list.sort()
target_num = int(input().rstrip())
target_list = list(map(int, input().split()))

answer = [ -1 for _ in range(target_num)]
for i in range(target_num):
    answer[i] =  binary_serch(target_list[i], 0, 0, card_num-1)

# 언패킹
print(*answer)

''' join
print(' '.join(map(str, answer)))
'''