import sys
sys.stdin = open('./input/5209.txt')

def choice_factory(cnt, cost):
    global min_cost
    if cost >= min_cost:
        return
    if cnt == product_num:
        if cost < min_cost:
            min_cost = cost
        return
    
    for j in range(product_num):  # 각 제품에 대해 공장을 하나 선택
        if not visited[j]:  # 해당 공장이 선택되지 않았다면
            visited[j] = True  # 공장 선택
            choice_factory(cnt + 1, cost + matrix[cnt][j])  # 다음 제품 선택
            visited[j] = False  # 백트래킹 (원상 복구)     

t = int(input())
for tc in range(1, t+1):
    product_num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(product_num)]

    min_cost = float('inf')
    visited = [False] * product_num

    choice_factory(0, 0)

    print(f'#{tc} {min_cost}')