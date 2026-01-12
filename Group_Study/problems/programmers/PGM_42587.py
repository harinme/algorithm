from collections import deque

def solution(priorities, location):
    arr = [0 for i in range(0,10)]
    top = 0
    for i in priorities:
        if i > top:
            top = i
        arr[i] += 1

  
    answer = 0
    dq = deque(priorities)
    while dq:
        check = dq.popleft()
        location -= 1
        if check == top:
            answer += 1

            if location < 0:
                return answer
            
            arr[top] -= 1
            if arr[top] == 0:
                for i in range(top-1,0,-1):
                    if arr[i] > 0:
                        top = i
                        break
        else:

            dq.append(check)
            if location < 0:
                location = len(dq) -1
           


    return answer

print(solution([2, 1, 3, 2],2))