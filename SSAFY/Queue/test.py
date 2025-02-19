from collections import deque


def find_last_pizza(queueSize, pizzas):
    queue = deque()
    for i in range(queueSize):
        """
        큐 안에 들어갈 원소: (피자 인덱스, 치즈 양)
        """
        queue.append((i, pizzas[i]))      # 처음 피자 다 넣었다

    nextPizzaIdx = queueSize

    while len(queue) > 1:
        pizzaIdx, cheese = queue.popleft()
        cheese //= 2
        if cheese > 0:      # 치즈가 덜 녹았다면
            queue.append((pizzaIdx, cheese))
        elif nextPizzaIdx < len(pizzas):
            queue.append((nextPizzaIdx, pizzas[nextPizzaIdx]))
            nextPizzaIdx += 1
    return queue[0][0] + 1


for caseNum in range(1, int(input()) + 1):
    queueSize, pizzaNum = map(int, input().split())
    pizzas = list(map(int, input().split()))
    output = find_last_pizza(queueSize, pizzas)

    print(f'#{caseNum} {output}')