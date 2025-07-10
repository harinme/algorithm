import sys
sys.stdin = open('test.txt')

#input = sys.stdin.readline

num = int(input().rstrip())

num_list = []
for _ in range(num):
    num_list.append(int(input().rstrip()))

print(num_list)