def solution(array, commands):
    answer = []
    while commands:
        x,y,z = commands.pop(0)
        sorted_array = sorted(array[x-1:y])
        num =  sorted_array[z-1]
        answer.append(num)
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
