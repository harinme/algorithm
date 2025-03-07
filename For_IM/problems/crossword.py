## 나중에 혼자 다시 풀어보기
import sys
sys.stdin = open('../input/crossword.txt')

t = int(input())

for tc in range(1, t + 1):
    puzzle_size, word_len = map(int, input().split())

    crossword = [list(map(int, input().split())) for _ in range(puzzle_size) ]
    # 흰색 1, 검은색 0 -> 입력 가능한 부분은 1
    counting = 0
    # 가로 탐색
    for x in range(puzzle_size):
        count = 0
        for y in range(puzzle_size):
            if crossword[x][y] == 1:
                count += 1
            else:
                if count == word_len:
                    counting += 1
                count = 0
        if count == word_len:
            counting += 1

    # 세로 탐색
    for y in range(puzzle_size):
        count = 0
        for x in range(puzzle_size):
            if crossword[x][y] == 1:
                count += 1
            else:
                if count == word_len:
                    counting += 1
                count = 0
        if count == word_len:
            counting += 1


    print(f'#{tc} {counting}')