'''
Q 구현하기
- 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
- 큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
- 1, 2, 3이 출력 되어야 함.
'''

# 1. append(), pop()
que = []
que.append(1)
que.append(2)
que.append(3)

print(que.pop(0), end=', ')
print(que.pop(0), end=', ')
print(que.pop(0))

# 1, 2, 3
print('---------' * 5)

# 2. queue 클래스 구현(원형 큐)
class queue():
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise IndexError('큐가 가득 찼습니다.')
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

qu = queue(3)

qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
# print(qu.items, qu.peek(), qu.get_size(), sep=', ')


print(qu.dequeue(), end=', ')
print(qu.dequeue(), end=', ')
print(qu.dequeue())
# print(qu.dequeue())
print('---------' * 5)

# 3. Deque(덱)
from collections import deque
dq = deque()

dq.append(2)
dq.appendleft(1)
dq.append(3)

# 앞에 숫자부터 앞쪽으로 삽입 [1, 2, 3, ..., ]
# dq.extendleft([3, 2, 1])

print(dq.popleft(), end=', ')
print(dq.popleft(), end=', ')
print(dq.popleft())