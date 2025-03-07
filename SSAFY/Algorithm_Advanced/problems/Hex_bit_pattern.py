import sys
sys.stdin = open('../input/Hex_bit_pattern.txt')

code_pattern = {
    '001101': 0,
    '010011': 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9
}
pattern_len = 6

t= int(input())
for tc in range(1, t+1):
    hex_str = input()
    bin_str = ''
    for i in hex_str:
        bin_str += format(int(i, 16), '04b')
    
    # 암호 패턴은 항상 1로 끝나기 때문에 0을 벗겨내더라도 문제가 생기는 건 앞에 0이 부족해지는 경우.
    bin_str = bin_str.strip('0')
    # 부족한 수만큼 0을 앞에 채워준다.
    if len(bin_str) % pattern_len != 0:
        bin_str = '0' * (pattern_len - (len(bin_str) % pattern_len)) + bin_str
    
    # 암호 패턴을 패턴의 길이(6)만큼 나누어준다.
    pattern_list = []
    for i in range(0, len(bin_str), pattern_len):
        pattern_list.append(bin_str[i:i+pattern_len])
    
    # 암호를 찾아준다.
    code = []
    for i in pattern_list:
        code.append(code_pattern[i])


    print(f'#{tc}', end=' ')
    print(*code)