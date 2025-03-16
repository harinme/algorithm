import sys
sys.stdin = open('./input/pre_order.txt')

def pre_order(node):
    if node:
        print(node, end=' ')
        pre_order(left[node])
        pre_order(right[node])

# 정점의 개수
V = int(input())

# 간선의 개수
E = V - 1

# 간선 정보
data = list(map(int, input().split()))

left = [False] * (V + 1)
right = [False] * (V + 1)

for i in range(E):
    # 부모, 자식
    p, c = data[i * 2], data[i * 2 + 1]
    
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
    

pre_order(1)
