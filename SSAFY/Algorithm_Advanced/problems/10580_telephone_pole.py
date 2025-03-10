import sys
sys.stdin = open('../input/10580_input.txt')

def cross_line(line_list):
    # 전선을 straight와 cross로 분리
    straight_list = []
    cross_list = []
    for a, b in line_list:
        if a == b:
            straight_list.append(a)
        else:
            cross_list.append((a, b))
    straight_list.sort()

    count = 0

    if not cross_line:
        return 0
    
    # (1) 교차선끼리의 교차 (O(N^2) 방식)
    for i in range(len(cross_list)):
        for j in range(i+1, len(cross_list)):
            x1, y1 = cross_list[i]
            x2, y2 = cross_list[j]
            # 조건: (x1 < x2 and y1 > y2) 또는 (x1 > x2 and y1 < y2)
            if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
                count += 1

    # (2) 직선과 교차선의 교차
    # 직선은 양쪽 전봇대에서 동일한 위치에 연결되므로,
    # cross 전선 (x, y)와 직선 a가 교차하려면 a가 두 좌표 사이에 있어야 함 (min(x,y) < a < max(x,y))
    for a in straight_list:
        for x, y in cross_list:
            if min(x, y) < a < max(x, y):
                count += 1

    return count


t = int(input())
for tc in range(1, t+1):
    line_num = int(input())

    line_list = []
    for i in range(line_num):
        line_list.append(list(map(int, input().split())))
                
    result = cross_line(line_list)
    

    print(f'#{tc} {result}')