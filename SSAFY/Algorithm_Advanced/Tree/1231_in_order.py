import sys
sys.stdin = open('./input/1231.txt')

def in_order(node):
    global word
    if node < len(tree):
        in_order(node * 2)
        word += tree[node]
        in_order(node * 2 + 1)

t = 10
for tc in range(1, t+1):
    v = int(input())
    tree = [False] * (v + 1)
    
    for _ in range(v):
        node_data = list(map(str, input().split()))
        node = int(node_data[0])
        value = node_data[1]
        tree[node] = value

    word = ''
    in_order(1)

    print(f'#{tc} {word}')