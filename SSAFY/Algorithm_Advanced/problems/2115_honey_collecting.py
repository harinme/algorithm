from pprint import pprint
import sys
sys.stdin = open('../input/2115_input.txt')

def find_max_num(honey_matrix):
    max_num = float('-inf')
    max_num_list = []
    for i in range(size):
        for j in range(size):
            if honey_matrix[i][j] == max_num:
                max_num_list.append([i, j])
            elif honey_matrix[i][j] > max_num:
                max_num = honey_matrix[i][j]
                max_num_list.clear()
                max_num_list.append([i, j])
    return max_num_list

def check_rounds(collect_range):
    




t = int(input())
for tc in range(1, t+1):
    size, collect_range, max_honey = map(int, input().split())
    honey_matrix = [list(map(int, input().split())) for _ in range(size)]

    # pprint(honey_matrix)

    # 무조건 큰 수가 포함되어야 한다.(탐욕?)
    # 큰 수 찾기
    max_num_list = find_max_num(honey_matrix)
    print(max_num_list)

    # 큰 수 주변 확인하기

    

    print(f'#{tc} ')