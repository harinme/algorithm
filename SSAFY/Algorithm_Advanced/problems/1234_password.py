import sys
sys.stdin = open('../input/1234_input.txt')

t = 10
for tc in range(1, t+1):
    str_len, password_txt = map(str, input().split())
    str_len = int(str_len)

    idx, top = 0, 0
    stack = []
    stack.append(password_txt[idx])

    while idx < str_len -1:
        idx += 1
        if stack:
        # 번호가 쌍이 아니라면
            if stack[top] != password_txt[idx]:
                stack.append(password_txt[idx])
                top += 1
            else: # 번호가 쌍을 이룬다면
                stack.pop(top)
                top -= 1
        else:
            stack.append(password_txt[idx])
            top += 1
    password = ''
    for i in stack:
        password += i

    print(f'#{tc} {password}')