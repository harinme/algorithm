import sys
sys.stdin = open('./input/5177.txt')
def sort(node):
    cur_node = node
    while cur_node >= 2:
        # 현재 노드가 짝수라면
        if cur_node % 2 == 0:
            p = cur_node // 2
            # 부모가 더 크다면?
            if tree[p]:
                if tree[p] > tree[cur_node]:
                    tree[p], tree[cur_node] = tree[cur_node], tree[p]
        else: # 홀수라면
            p = (cur_node - 1) // 2
            if tree[p]:
                # 부모가 더 크다면?
                if tree[p] > tree[cur_node]:
                    tree[p], tree[cur_node] = tree[cur_node], tree[p]
        cur_node = p


def insert(value):
    global node
    tree[node] = value
    sort(node)
    node += 1

def root_sum(child):
    global total
    if child >= 2:
        # 자식이 짝수라면
        if child % 2 == 0:
            p = child // 2
        else: # 홀수라면
            p = (child - 1) // 2
        total += tree[p]
        root_sum(p)


t = int(input())
for tc in range(1, t+1):
    # 부모 노드의 값 < 자식 노드의 값
    V = int(input())
    tree = [False] * (V+1)
    data = list(map(int, input().split()))

    node = 1
    # 트리 채우기
    for i in data:
        insert(i)
    
    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    total = 0
    root_sum(V)

    print(f'#{tc} {total}')