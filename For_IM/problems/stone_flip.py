import sys
sys.stdin = open('../input/stone_flip.txt')


'''동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.

i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

[입력]
첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
(1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)'''

t = int(input())

for tc in range(1, t+1):

    stone_num, flip_num = map(int, input().split())
    stone_staus = list(map(int, input().split()))


    for mc in range(flip_num):

        target_idx, target_range = map(int, input().split())

        for i in range(1, target_range+1):
            b_stone = target_idx -1 - i
            n_stone = target_idx -1 + i
            if 0 <= b_stone < stone_num and 0 <= n_stone < stone_num:
                if stone_staus[b_stone] == stone_staus[n_stone]:
                    if stone_staus[b_stone] == 0:
                        stone_staus[b_stone], stone_staus[n_stone] = 1, 1
                    else:
                        stone_staus[b_stone], stone_staus[n_stone] = 0, 0
            else:
                break

    stone =''
    for i in stone_staus:
        i = str(i)

        stone += ''.join(i)

    print(f'#{tc} {" ".join(stone)}')