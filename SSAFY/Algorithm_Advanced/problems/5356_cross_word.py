import sys
sys.stdin = open('../input/5356_input.txt')

t = int(input())
for tc in range(1, t+1):
    word_num = 5
    word_matrix = [list(map(str, input().strip())) for _ in range(word_num)]

    max_len = -1
    for i in word_matrix:
        if len(i) > max_len:
            max_len = len(i)

    cross_word = ''
    for i in range(max_len):
        for j in range(word_num):
            # 인덱스 범위를 벗어난다면?
            if i > len(word_matrix[j]) -1:
                continue
            cross_word += word_matrix[j][i]

    print(f'#{tc} {cross_word}')