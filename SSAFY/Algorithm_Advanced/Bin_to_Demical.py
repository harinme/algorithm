import sys
sys.stdin = open('Bin_to_Demical.txt')

target_str = str(input())
slice_num = 7

for i in range(0, len(target_str), slice_num):
    bin_str = target_str[i : i + slice_num]
    demical_str = int(bin_str, 2)
    
    print(demical_str, end=' ')
