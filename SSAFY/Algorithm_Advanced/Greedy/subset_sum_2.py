import sys
sys.stdin = open('./input/subset_sum.txt')

def recur(start, cnt):
    if cnt == len(arr):
        path = []
        for i in range(len(arr)):
            if used[i]==True:
                path.append(arr[i])
        if sum(path)==0:
            print(*path)
        return
    
    for i in range(start, len(arr)):
        used[i] = True
        recur(i+1, cnt+1)

        used[i] = False
        recur(i+1, cnt+1)
        

arr = list(map(int, input().split()))
used = [False] * len(arr)
recur(0,0)

