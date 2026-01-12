def solution(progresses, speeds):
    answer = []
    
    days = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i] 
        day = remain // speeds[i]      
        if remain % speeds[i] != 0:    
            day += 1
        days.append(day)

    i = 0
    while i < len(days):
        count = 1  
        current_day = days[i] 
        

        j = i + 1
        while j < len(days) and days[j] <= current_day:
            count += 1
            j += 1
        
        answer.append(count)
        i = j  
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]