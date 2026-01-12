def solution(citations):
    answer = 0
    max_num = max(citations)
    counting = [0 for _ in range(max_num + 1)]
    for i in citations:
        for j in range(0, i + 1):
            counting[j] += 1

    # print(counting)
    max_h = 0
    for i in range(len(counting)):
        if counting[i] >= i:
            max_h = i
        else:
            return max_h
    return max_h

print(solution([3, 0, 6, 1, 5])) # 3