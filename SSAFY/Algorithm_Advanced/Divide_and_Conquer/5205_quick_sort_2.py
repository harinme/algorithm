import sys
sys.stdin = open('./input/5205.txt')

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = arr[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
    arr[start], arr[right] = arr[right], arr[start]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1,end)

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')