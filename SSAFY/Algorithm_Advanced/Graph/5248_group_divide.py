import sys
sys.stdin = open('./input/5248.txt')

def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        parent[b_root] = a_root

t = int(input())
for tc in range(1, t+1):
    human_num, request = map(int, input().split())
    data = list(map(int, input().split()))
    
    # 자신의 루트 정보(부모)를 담을 리스트를 생성
    # 자기 자신의 번호를 인덱스 그대로 사용하고 싶어서 +1
    parent = [i for i in range(human_num+1)]
    
    # data를 부모 자식으로 나눠서 함께 저장
    request_list = []
    for i in range(request):
        p, c = data[i * 2], data[i * 2 + 1]
        union(p, c)
    
    # 각 노드 별 최상단 루트로 경로 압축시킴.
    # (A-B, B-C 일때 union을 하면, 각 진행한 얘들끼리만 정보가 업데이트 됨. A-C는 연결 못 함)
    # (A-C를 연결하는 과정)
    for i in range(1, human_num+1):
        find_root(i)

    # 0번 인덱스는 사용하지 않으니 삭제
    parent.pop(0)
    # 중복을 제거하면 자연스럽게 각 그룹이 나누어짐.
    parent = set(parent)
    
    print(f'#{tc} {len(parent)}')