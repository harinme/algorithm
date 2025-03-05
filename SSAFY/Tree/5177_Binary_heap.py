import sys
sys.stdin = open('5177_input.txt')

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    tree = [0] * (N + 1)
    values = list(map(int, input().split()))
    
    tree[1] = values.pop(0)
    node = 2
    
    while values:
        tree[node] = values.pop(0)
        # 짝수 노드라면(왼쪽)
        if node % 2 == 0:
            # 부모가 현재 노드보다 크다면 서로 바꿔줘라
            if tree[node/2] > tree[node]:
                tree[node/2], tree[node] = tree[node], tree[node/2]
        else: # 오른쪽 노드라면
            if tree[(node-1)/2] > tree[node]:
                tree[(node-1)/2], tree[node] = tree[node] > tree[(node-1)/2]
        
    print(tree)
                
        



    
    print(f'#{tc} ')