import sys
sys.stdin = open('../input/3499_perfect_suffle.txt')

t = int(input())

for tc in range(1, t+1):
    card_num = int(input())
    card_list = list(map(str, input().split()))
    num = (card_num+1) // 2
    suffle_deck = []

    card_A = card_list[:num]
    card_B = card_list[num:]
    for a, b in zip(card_A, card_B):
        suffle_deck.extend([a, b])

    if len(card_A) > len(card_B):
        suffle_deck.append(card_A[-1])

    print(f'#{tc} {" ".join(suffle_deck)}')