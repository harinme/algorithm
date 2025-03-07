import sys
sys.stdin = open('../input/5185_input.txt')
t = int(input())
for tc in range(1, t+1):
    hex_len, hex_str  = map(str, input().split())
    hex_len = int(hex_len)
    dec_num = 0
    bin_str = ''

    for i in range(hex_len):
        dec_num = int(hex_str[i], 16) 
        bin_str += str(format(dec_num, '04b'))
        

    print(f'#{tc} {bin_str}')