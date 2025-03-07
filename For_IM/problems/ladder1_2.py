import sys
sys.stdin = open('../input/ladder1_2_input.txt')

for _ in range(10):
    test_case= int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

       #  상, 좌, 우
    dx = [-1, 0, 0]
    dy = [ 0,-1, 1]

    start = 0
    for i in range(len(ladder_matrix[99])):
        if ladder_matrix[99][i] == 2:
            start = i
    x, y = 99, start

    dir = 0
    for i in range(100):
        for j in range(100):
            
            nx, ny = i + dx[dir] , j + dy[dir]
            if  0 <= nx and 0<= ny <100 and ladder_matrix[nx][ny] ==1 :
                
                 