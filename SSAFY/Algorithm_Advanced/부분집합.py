#친구 5명 중에서 적어도 2명이상과 함께 카페를 가는 경우의 수는?
friends = {'A', 'B', 'C', 'D', 'E'}
total = 2 ** len(friends)

# 전체 경우의 수에서 1명만 데려가는 경우 + 아무도 안 데려가는 경우를 빼면 된다.
# 1명만 데려가는 경우는 5, 아무도 안 데려가는 경우는 1
total = total - len(friends) - 1
print(total)

##---------------------------------------
friends = {'A', 'B', 'C', 'D', 'E'}
n = len(friends)

def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    '''
    for i in range(n):
        if (tar >> i) 0x1:
            cnt +=1
    '''
    return cnt


# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
# 모든 부분 집합을 확인
for target in range(1<<n):
# 만약, 원소의 개수가 2개 이상이면 answer +=1
    if get_count(target) >= 2:
        answer +=1
print(answer)


### 5명 중에서 3명을 뽑는 경우
arr = ['A', 'B', 'C', 'D', 'E']
n = 3

path = []

def recur(cnt, start):
    # N명을 뽑는 경우
    if cnt == 3:
        print(*path)
        return
    
    # for i in range(이전에 뽑았던 인덱스 +1 , len(arr)):
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i + 1)
        path.pop()
    
recur(0, 0)

# 주사위 던지기
arr = [1, 2, 3, 4, 5, 6]
n = 3

path = []

def recur(cnt, start):
    if cnt == 3:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i)
        path.pop()


recur(0, 0)


