import sys
sys.stdin = open('traversal.txt')

def pre_order(focus):
    if focus:
        print(focus)
        pre_order(left[focus])
        pre_order(right[focus])
# 정점의 개수
V = int(input())

# 간선의 개수 = 정점의 개수 -1
E = V - 1

data = list(map(int, input().split()))

# 부모를 기준으로 자식 저장
left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    # p = parent / c = child
    p, c = data[i * 2], data[i * 2 + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c 


pre_order(1) 