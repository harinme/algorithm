import sys
sys.stdin = open('../input/baby_gin.txt')

def is_baby_gin(target):
    cnt = 0
    left = target[:len(target)//2]
    right = target[len(target)//2:]

    left.sort()
    right.sort()

    if left[0] == left[1] == left[2]:
        cnt +=1
    if right[0] == right[1] == right[2]:
        cnt +=1
    
    if sum(left) == (left[-1] -1) * 3:
        cnt +=1
    if sum(right) == (right[-1] -1) * 3:
        cnt +=1
    
    return cnt == 2

def recur(cnt):
    global result
    if result == 1:
        return
    
    if cnt == 6:
        if is_baby_gin(path):
            result = 1
        return
    
    for i in range(len(card_list)):
        if used[i] == True:
            continue
        used[i] = True
        path.append(card_list[i])
        recur(cnt+1)

        used[i] = False
        path.pop()


        




    


t = int(input())
for tc in range(1,t+1):
    card_list = list(map(int, input().strip()))
    result = 0
    
    path = []
    used = [False] * len(card_list)

    if is_baby_gin(card_list):
        print(f'#{tc} baby-gin')
    else:
        recur(0)
        if result == 1:
            print(f'#{tc} baby-gin')
        else:
            print(f'#{tc} not_baby-gin')
