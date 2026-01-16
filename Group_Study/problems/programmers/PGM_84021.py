from pprint import pprint
from collections import deque
# 테이블에 있는 것과 딱 맞는 위치를 찾아라!

def solution(game_board, table):
    # 1단계 테이블에서 각 조각들을 추출한다.
    # 2단계 하나씩 대입해본다!(회전도 시켜서 해서 맞는 구멍이 있는지 체크)
    
    
    def get_pieces(table):
        n = len(table)
        visited = [[False]*n for _ in range(n)]
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        pieces = []

        for i in range(n):
            for j in range(n):
                if table[i][j] == 1 and not visited[i][j]:
                    queue = deque()
                    queue.append((i,j))
                    visited[i][j] = True
                    piece = [(i,j)]
                    
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dir:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                piece.append((nx, ny))

                    # 비교하기 쉽게 0,0으로 맞춰줌
                    min_x = min(x for x, y in piece)
                    min_y = min(y for x, y in piece)
                    piece = [(x - min_x, y - min_y) for x, y in piece]  
                    pieces.append(piece)
        return pieces

    def rotate(piece):
        rotated = [(y, -x) for x, y in piece] # 90도 회전

        min_x = min(x for x, y in rotated)
        min_y = min(y for x, y in rotated)
        rotated = [(x - min_x, y - min_y) for x, y in rotated]

        return rotated


    game_pieces = get_pieces(table)
    board_holes = get_pieces([[1-x for x in row] for row in game_board])
    answer = 0
    used = [False]*len(game_pieces)

    for hole in board_holes:
        for i in range(len(game_pieces)):
            if used[i]:
                continue
            matched = False
            piece_rot = game_pieces[i]
            for _ in range(4):
                piece_rot = rotate(piece_rot)
                # 좌표 리스트를 정렬하면 순서가 달라도 같은 모양이면 비교 가능
                if sorted(piece_rot) == sorted(hole): 
                    answer += len(game_pieces[i])               # 맞춘 조각 크기 더하기
                    used[i] = True                     # 사용 완료
                    matched = True
                    break
            if matched:
                break

    return answer

# 14
print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]] ))

#0
print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))