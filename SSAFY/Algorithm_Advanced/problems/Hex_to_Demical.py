import sys
sys.stdin = open('../input/Hex_to_Demical.txt')

t = int(input())
for tc in range(1, t+1):
    hex_str = input()
    bin_str =''
    # 16 -> 10 -> 2
    for i in hex_str:
        bin_str += format(int(i, 16), '04b')

    # 몇 비트씩 묶을지
    bit = 7
    decimal_list=[]

    # 추가 조건 충족을 위한 과정
    ''' 추가 조건
    만약 자른 7비트가 '0000000'이면, 실제로는 '0000'(앞4비트)만 버리고
    뒤3비트('000')는 다음 chunk와 합쳐서 진행하기
    '''
    for i in range(0, len(bin_str), bit):
        end_idx = i + bit
        if bin_str[i: end_idx] == '0000000':
            bin_str = bin_str[:i] + bin_str[end_idx-3:]

    # 각 7비트 씩 묶어서 나눠주기
    for i in range(0, len(bin_str), bit):
        end_idx = i + bit
        # 인덱스 범위를 벗어나지 않게 처리
        if end_idx > len(bin_str):
            decimal_list.append(bin_str[i:])
        else:
            decimal_list.append(bin_str[i:end_idx])


    # 리스트에서 하나씩 꺼내 십진수로 변환해주기
    for i in range(len(decimal_list)):
        decimal_list[i] = int(decimal_list[i], 2)
    
    print(f'#{tc} ', end='')
    print(*decimal_list)