import sys
sys.stdin = open('5176_input.txt')

def inorder(node):
    if node <= N:
        global num
        # 왼쪽 노드 우선
        inorder(node * 2)
        tree[node] = num
        num += 1
        inorder(node * 2 + 1)

t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    
    tree = [0] * (N + 1)
    num = 1

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')