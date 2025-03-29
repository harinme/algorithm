import sys
sys.stdin = open('./input/5202.txt')
t= int(input())
for tc in range(1, t+1):
    request_num = int(input())
    request_list = []
    for i in range(request_num):
        s, e = map(int, input().split())
        request_list.append((s, e))

    request_list.sort(key=lambda x: (x[1], x[0]))

    cnt = 1
    s, e = request_list.pop(0)

    hold = e
    for req_s, req_e in request_list:
        if req_s >= hold:
            cnt += 1
            hold = req_e

    print(f'#{tc} {cnt}')