import sys
sys.stdin = open('./input/5174.txt')

def subtree(node):
    global count
    if node:
        count += 1
        subtree(left[node])
        subtree(right[node])


t = int(input())
for tc in range(1, t+1):
    E, target_root = map(int, input().split())
    data = list(map(int, input().split()))
    V = E + 1

    left = [False] * (V + 1)
    right = [False] * (V + 1)
    for i in range(E):
        p, c = data[i * 2], data[i * 2 + 1]
        if not left[p] :
            left[p] = c
        else:
            right[p] = c
    
    count = 0
    subtree(target_root)
    

    print(f'#{tc} {count}')