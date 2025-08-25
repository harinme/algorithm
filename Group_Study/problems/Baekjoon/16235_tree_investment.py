import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def spring():
    # 자신의 나이만큼 양분 흡수, 흡수 가능하면 나이 +1 못하면 사망
    pass


def summer():
    pass

def autumn():
    pass

def winter():
    pass

# 땅 너비, 초기 나무, 몇 년 후
ground, seed, after = map(int, input().split())

trees = list([[ ] for _ in range(ground)] for _ in range(ground))
food = [[5 for _ in range(ground)] for _ in range(ground)]
plus = [list(map(int,input().split())) for i in range(ground)] 

print(plus)

# for i in range(seed):
#     x, y, z = map(int, input().split())


'''
1 ≤ N ≤ 10
1 ≤ M ≤ N2
1 ≤ K ≤ 1,000
1 ≤ A[r][c] ≤ 100
1 ≤ 입력으로 주어지는 나무의 나이 ≤ 10
입력으로 주어지는 나무의 위치는 모두 서로 다름
'''
print(ground, seed, after) 