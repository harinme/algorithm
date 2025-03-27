import sys
sys.stdin = open('./input/5204.txt')

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    l_idx, r_idx = 0, 0
    sorted_arr = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            sorted_arr.append(left[l_idx])
            l_idx += 1
        elif left[l_idx] == right[r_idx]:
            sorted_arr.append(left[l_idx])
            l_idx += 1
            sorted_arr.append(right[r_idx])
            r_idx += 1
        else:
            sorted_arr.append(right[r_idx])
            r_idx += 1
    sorted_arr.extend(left[l_idx:])
    sorted_arr.extend(right[r_idx:])
    return sorted_arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

t = int(input())
for tc in range(1, t+1):
    num_len = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[num_len//2]} {cnt}')
