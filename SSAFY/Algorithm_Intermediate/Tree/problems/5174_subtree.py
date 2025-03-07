import sys
sys.stdin = open('../input/5174_input.txt')

t = int(input())

for tc in range(1, t+1):
    E, N = map(int, input().split())
    V = E + 1
    data = list(map(int, input().split()))

    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        p, c = data[i * 2], data[i * 2 + 1]
        
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    
    # 현재 문제에서 필요는 x
    # # 부모가 없는 노드가 전체의 루트 노드가 된다. 
    # # 즉, 자식에서는 나타나지 않고 부모에서만 나타나는 노드가 루트 노드이다.
    # parents = set()
    # for i in range(0, len(data), 2):
    #     parents.add(data[i])

    # childs = set()
    # for i in range(1, len(data), 2):
    #     childs.add(data[i])
    
    # # set의 '-' = 차집합
    # roots = parents - childs
    # root = roots.pop()
    
    # 재귀로 한다면
    # def pre_order(T):
    #     if T == 0:  # 노드가 없는 경우
    #        return 0
    #     return 1 + pre_order(left[T]) + pre_order(right[T])
    
    def pre_order(T, count):
        if T:
            count[0] += 1
            pre_order(left[T], count)
            pre_order(right[T], count)
        return count
    
    count = [0]
    pre_order(N, count)

    print(f'#{tc} {count.pop()}')