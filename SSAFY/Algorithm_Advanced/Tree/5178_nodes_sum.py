import sys
sys.stdin = open('./input/5178.txt')

# 자식이 노드의 정보가 미리 입력되어있지 않으면,
# 부모 노드가 생성될 수 없으므로 후위 순회
def post_order(node):
    if node <= V:
        post_order(node * 2)
        post_order(node * 2 + 1)
        if not tree[node]:
            if node * 2 + 1 <= V:
                tree[node] = tree[node * 2] + tree[node * 2 + 1]
            else:
                tree[node] = tree[node * 2]

t = int(input())
for tc in range(1, t+1):
    V, leaf_node_num, target_node = map(int, input().split())
    E = V-1
    tree = [False] * (V + 1)

    # leaf 노드만 먼저 채워줌
    for _ in range(leaf_node_num):
        node, value = map(int, input().split())
        tree[node] = value
    
    post_order(1)

    print(f'#{tc} {tree[target_node]}')