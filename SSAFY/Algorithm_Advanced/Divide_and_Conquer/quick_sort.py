import sys
sys.stdin = open('./input/quick_sort.txt')

def quick_sort(arr, start, end):
    
    if start < end:
        pivot_idx = partition(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]


    
    arr[start], arr[right] = arr[right], arr[start]
    return right


t = int(input())
for tc in range(1, t+1):
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data)-1)
    
    print(f'#{tc} {data}')