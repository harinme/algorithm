import sys
sys.stdin = open('../input/5201_input.txt')

def choice_container(idx, truck_list):
    global container_list
    global total
    possible_container = []
    if container_list:
        for i in range(len(container_list)):
            if container_list[i] <= truck_list[idx]:
                possible_container.append(container_list[i])

        if len(possible_container)>=1:
            possible_container.sort()
            total += possible_container.pop()
            container_list.clear
            container_list = possible_container
            return
        else:
            return
    else:
        return


t = int(input())
for tc in range(1, t+1):
    container_num, truck_num = map(int, input().split())
    container_list = list(map(int, input().split()))
    container_list.sort()
    truck_list = list(map(int, input().split()))
    truck_list.sort(reverse= True)
    total = 0
    idx = 0
    
    while idx <= truck_num-1 and len(container_list) >= 1:
        choice_container(idx, truck_list)
        idx += 1

    print(f'#{tc} {total}')