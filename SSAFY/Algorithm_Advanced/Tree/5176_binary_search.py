import sys
sys.stdin = open('./input/5176.txt')

def inorder(node):
    global num
    if node <= V:
        inorder(node * 2)
        tree[node] = num
        num += 1
        inorder(node * 2 + 1)

t = int(input())
for tc in range(1, t+1):
    V = int(input())
    E = V - 1
    tree = [False] * (V + 1)

    num = 1
    inorder(1)


    print(f'#{tc} {tree[1]} {tree[V//2]}')