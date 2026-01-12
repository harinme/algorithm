from collections import deque
def solution(prices):
    dq = deque(prices)
   
    answer = []
    while dq:
        time = 0
        check = dq.popleft()
        
        if not dq:
            answer.append(time)
            return answer

        for i in dq:
            time += 1
            if i < check:
                break
        answer.append(time)
    


    return answer


print(solution([1, 2, 3, 2, 3])) #[4, 3, 1, 1, 0]