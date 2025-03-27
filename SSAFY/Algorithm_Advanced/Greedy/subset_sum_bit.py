import sys
sys.stdin = open('../input/subset_sum.txt')

int_list = list(map(int, input().split()))

def get_subset(target):
    tar = target
    subset = []
    for i in range(len(int_list)):
        if tar & 0x1:
            subset.append(int_list[i])
        tar >>= 1
    return subset

for i in range(1<<len(int_list)):
    if sum(get_subset(i)) == 0:
        print(get_subset(i))
        