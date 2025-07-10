import sys
sys.stdin = open('test.txt')
#input = sys.stdin.readline

'''
퀵 정렬(메모리 초과)
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= end and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        # 만약 교차하지 않는다면 swqp
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[start], arr[right] = arr[right], arr[start]

    quick_sort(arr, start, right -1)
    quick_sort(arr, right +1, end)



num = int(input().rstrip())

num_list = []
for _ in range(num):
    num_list.append(int(input().rstrip()))

quick_sort(num_list, 0, len(num_list)-1)
for i in num_list:
    print(i)
'''

num = int(input().rstrip())

# 수의 범위가 지정되어 있으니 차라리 그거에 대한 배열을 만들고 누적합으로 하는게 메모리 사용량이 적다.
count_list = [0]* 10001

for _ in range(num):
    number = int(input().rstrip())
    count_list[number] += 1

for i in range(len(count_list)):
    if count_list[i] == 0:
        continue
    while count_list[i] > 0:
        print(i)
        count_list[i] -=1