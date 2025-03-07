import sys
sys.stdin = open('../input/5099_input.txt')

t = int(input())

for tc in range(1, t+1):
    oven_size, pizza_total_num = map(int, input().split())
    pizza_list = list(map(int, input().split()))

    oven = []
    for i in range(1, oven_size+1):
        oven.append((i, pizza_list.pop(0)))

    next_pizza = oven_size + 1
    
    while len(oven) > 1: 
            pizza_num, cheese = oven.pop(0)
            cheese = cheese //2
            # 피자가 다 녹았다면?
            if cheese <=0:
                # 새로운 피자가 남아있으면 새로운 피자를 넣어라!
                if pizza_list:
                    oven.append((next_pizza, pizza_list.pop(0)))
                    next_pizza += 1
                # 피자가 안 남았으면 그냥 계속 굽기만 하면 됨.
            # 피자가 다 안 녹았다면?
            else: # 그냥 그대로 뒤로 다시 넣어주면서 굽기
                oven.append((pizza_num, cheese))
    
    # 이제 오븐에 하나만 남게 됐다면?
    # oven = [(pizza_num, cheese)]
    result = oven[0][0]

    print(f'#{tc} {result}')