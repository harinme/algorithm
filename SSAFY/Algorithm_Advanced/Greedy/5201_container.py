import sys
sys.stdin = open('./input/5201.txt')

def dock():
    global truck_list
    global container_list
    global total
    hold = truck_list.pop()
    can = []
    for i in container_list:
        if i <= hold:
            can.append(i)
    container_list = can
    if len(can)==0:
        return
    else:
        can.sort()
        total+=can.pop()
        return
    

t= int(input())
for tc in range(1, t+1):
    container_num, truck_num = map(int, input().split())
    container_list = list(map(int, input().split()))
    container_list.sort()

    
    truck_list = list(map(int, input().split()))
    truck_list.sort()

    total= 0

    while truck_list and container_list:
        dock()
    
    print(f'#{tc} {total}')