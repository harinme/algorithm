import sys
sys.stdin = open('./input/5205.txt')

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        # left: 피벗보다 작거나 같은 원소를 건너뛰기
        while left <= end and arr[left] <= pivot:
            left += 1
        
        # right: 피벗보다 크거나 같은 원소를 건너뛰기
        while left <= right and arr[right] >= pivot:
            right -= 1
        
        # 만약 포인터가 교차하지 않았다면 swap
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    # 피벗을 올바른 위치에 배치 (right 위치와 swap)
    arr[start], arr[right] = arr[right], arr[start]

    # 피벗을 기준으로 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


t = int(input())
for tc in range(1, t+1):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, arr_len-1)

    print(f'#{tc} {arr[arr_len//2]}')