import sys
from pprint import pprint
from collections import deque
sys.stdin = open('5105_input.txt')

def find_start_goal(maze, maze_size):
    start, goal = None, None

    for i in range(maze_size):
        for j in range(maze_size):

            if start != None and goal != None:
                return start, goal
            if maze[i][j] == 2:
                start = (i, j)
            if maze[i][j] == 3:
                goal = (i, j)

def maze_game(start, goal, maze, maze_size):
    maze_size = count


t = int(input())

for tc in range(1, t+1):
    maze_size = int(input())
    maze = [list(map(int, input().strip())) for _ in range(maze_size)]

    start, goal = find_start_goal(maze, maze_size)
    maze_game(start, goal, maze, maze_size)



    pprint(maze)
    print(f'#{tc} {start}, {goal}')