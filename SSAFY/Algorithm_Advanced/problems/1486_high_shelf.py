import sys
sys.stdin = open('../input/1486_input.txt')

def min_number(cur_height):
    global min_height
    if cur_height >= height:
        if cur_height < min_height:
            min_height = cur_height
        return

    for i in range(human_num):
        if used[i]:
            continue
        # 중복 방지를 위한 조건: 
        # 이전 인덱스와 같은 값인데, 이전 값이 선택되지 않았다면 이번 값을 건너뛰기
        if i > 0 and human_list[i] == human_list[i-1] and not used[i-1]:
            continue

        used[i] = True
        min_number(cur_height + human_list[i])
        used[i] = False

t = int(input())
for tc in range(1, t+1):
    human_num, height = map(int, input().split())
    human_list = list(map(int, input().split()))
    
    # 중복 제거를 위해 정렬 (작은 값 또는 큰 값 순 모두 가능하지만, 
    # 보통은 문제에 따라 정렬 방향을 결정하면 좋습니다)
    human_list.sort()
    
    used = [False] * human_num
    min_height = sum(human_list)
    
    min_number(0)
    result = min_height - height

    print(f'#{tc} {result}')
