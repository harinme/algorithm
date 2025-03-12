import sys
sys.stdin = open('../input/baby_gin.txt')

def is_baby_gin(cards):
    cnt = 0
    left = cards[:3]
    right = cards[3:]
    cards=[left, right]

    for i in range(2):
        if cards[i][0] == cards[i][1] == cards[i][2]:
           cnt += 1
        elif sum(cards[i]) == (max(cards[i])-1) * 3:
            cnt += 1
    return cnt == 2

def recur(cnt):
    global baby_gin_result
    # 이걸 넣어서 이미 그 전 조합에서 이미 판별이 난 거면 남아있던 함수 호출들을 끝내기 위해서
    if baby_gin_result == True:
        return
    
    if cnt == 6:
        if is_baby_gin(path):
            baby_gin_result = True
        return 
    
    for idx in range(len(card_list)):
        if used[idx] == True:
            continue
        used[idx] = True
        path.append(card_list[idx])
        recur(cnt+1)
        path.pop()
        used[idx] = False



t = int(input())
for tc in  range(1, t+1):
    card_list = list(map(int, input().strip()))
    path = []
    used = [False] * len(card_list)
    baby_gin_result = False

    
    # 처음에 바로 들어온 값에서 baby_gin인지 확인하고 맞으면 끝내고 아니면 추가로 확인
    if is_baby_gin(card_list):
        print(f'#{tc} 1')
    else:
        recur(0)
        if baby_gin_result == True:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')