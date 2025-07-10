import sys
from pprint import pprint
sys.stdin = open('test.txt')
# input = sys.stdin.readline

n = int(input().rstrip())

target = int(input().rstrip())

'''
이동 방향의 규칙성
1, 1, 2, 2, 3, 3, 4, 4, 5 ...
1칸 위로, 1칸 오른쪽으로, 2칸 아래로, 2칸 왼쪽으로, 3칸 위로, ...

방향의 순서 (상, 우, 하, 좌)

따라서 상우하좌의 순서대로 방향 전환이 들어가고
그 전환 규칙은 카운팅 변수를 만들어서 1이 두번 나오면 이후에 2칸 이동으로 바꾸는 형식
'''

# 반복이 끝날 기준
max_num = n**2 

# 현재 기입될 숫자
c_num = 2
c_dir = 0
max_count = 1
tx, ty = 0, 0
## 이걸 안 하면 1일 때 체크를 안해둬서 틀리게 됨
if target == 1:
    tx, ty = n//2 + 1, n//2 +1

# 시작될 위치
snail_matrix = [[0 for _ in range(n)] for _ in range(n)]
 
start = n//2
snail_matrix[start][start] = 1
dx, dy = start, start
# pprint(snail_matrix)

while c_num <= max_num:
    
    c_dir = c_dir % 4

    dir = [
        (-1, 0), # 상
        (0, 1), # 우
        (1, 0), # 하
        (0, -1) # 좌
    ]
    for _ in range(2):
        for _ in range(max_count):
            dx = dx + dir[c_dir][0]
            dy = dy + dir[c_dir][1]
            if not 0 <= dx < n and 0 <= dy < n:
                break
            if c_num == target:
                tx, ty = dx+1, dy+1
            snail_matrix[dx][dy] = c_num
            c_num +=1
        c_dir += 1
            
    max_count+= 1



for i in snail_matrix:
    print(*i)

print(tx, ty)