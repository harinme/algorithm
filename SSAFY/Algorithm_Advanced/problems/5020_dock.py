import sys
sys.stdin = open('../input/5020_input.txt')

t = int(input())
for tc in range(1, t+1):
    request_num = int(input())
    request_list = []
    for _ in range(request_num):
        request_list.append(list(map(int, input().split())))

    request_list.sort( key= lambda x : x[1])

    # 작업 시간이 가장 빨리 끝나는 순서대로 픽한다
    # 정렬할 때 x[1]은 종료시간 기준으로 정렬했으므로 맨 앞에 있는 건 무조건 픽한다.
    s, e = request_list.pop(0)
    cnt = 1
    for request in request_list:
        # [0]은 시작 시간 / [1]은 끝나는 시간
        # 다음 요청의 시작 시간이 그전에 픽한 작업의 끝나는 시간이랑 같거나 그 이후에 시작하는 거라면 픽!
        if request[0] >= e:
            # e 는 그 작업의 끝나는 시간으로 갱신한다.
            e = request[1]
            cnt += 1

    print(f'#{tc} {cnt}')