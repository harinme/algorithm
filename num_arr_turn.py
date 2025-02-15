from pprint import pprint
import sys

sys.stdin = open('num_arr_turn.txt')

def turn(matrix ,degree):
    matrix_turn = list(map(list, zip(*matrix[::-1])))
    if degree >= 180:
        matrix_turn = list(map(list, zip(*matrix_turn[::-1])))
        if degree >= 270:
            matrix_turn = list(map(list, zip(*matrix_turn[::-1])))
    return matrix_turn


t= int(input())
for tc in range(1, t+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    matrix_90 = turn(matrix, 90)
    matrix_180 = turn(matrix, 180)
    matrix_270 = turn(matrix, 270)


    print(f'#{tc}')
    for x, y, z in zip(matrix_90, matrix_180, matrix_270):
        total_1 = ''.join(str(j) for j in x)
        total_2 = ''.join(str(j) for j in y)
        total_3 = ''.join(str(j) for j in z)
        print(total_1, total_2, total_3)