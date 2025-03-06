import sys
sys.stdin = open('1225_input.txt')

def code(code_list):
    while True:
        for i in range(1, 6):
            num = code_list.pop(0)
            num -= i
            if num <= 0:
                num = 0
                code_list.append(num)
                return code_list
            code_list.append(num)

t = 10
for _ in range(t):
    tc = int(input())
    code_total_num = 8
    code_list = list(map(int, input().split()))

    code(code_list)

    

    print(f'#{tc}', end=' ')
    for i in code_list:
        print(i, end=' ')
    print()