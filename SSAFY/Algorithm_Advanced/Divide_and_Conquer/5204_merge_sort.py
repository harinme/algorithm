import sys
sys.stdin = open('./input/5204.txt')

def merge(left, right):
    global count
    
    if left and right:
        if left[-1] > right[-1]:
            count += 1

    merged_arr = []
    left_idx, right_idx = 0, 0
    left_size, rigth_size = len(left), len(right)

    while left_idx < left_size and right_idx < rigth_size:
        if left[left_idx] <= right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1
    merged_arr.extend(left[left_idx:])
    merged_arr.extend(right[right_idx:])

    return merged_arr

def merge_sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
       return arr
    
    mid = arr_len // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


t = int(input())
for tc in range(1, t+1):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    count = 0

    sorted_arr = merge_sort(arr)

    print(f'#{tc} {sorted_arr[arr_len//2]} {count}')