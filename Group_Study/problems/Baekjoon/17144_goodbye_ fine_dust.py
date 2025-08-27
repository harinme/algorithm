from pprint import pprint
import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline


x, y, after = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(x)]

pprint(room)
air_circle_top = -1
air_circle_bottom = -1
for i in range(x):
    if room[i][0] == -1:
        air_circle_top, air_circle_bottom = i, i +1
        break

print(air_circle_bottom)