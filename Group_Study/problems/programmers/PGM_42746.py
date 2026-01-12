def solution(numbers):
    array = []
    for i in numbers:
        array.append(str(i))
        ''' 문자열 비교는 길이 상관 없이 사전순으로 비교(앞에서 부터 한글자씩 비교)
    "3333" vs "3030"
    ↓ 첫 글자: '3' = '3' (같음)
    ↓ 둘째 글자: '3' > '0' (여기서 결정!)
    '''
    array.sort(key = lambda x :  x*10, reverse=True)
    answer = ''
    for i in array:
        answer += i
        ## 0 0 0 과 같이 0만 주어진 경우도 생각해야함
    return(str(int(answer)))

print(solution([6, 10, 2])) # "6210"
print(solution([3, 30, 34, 5, 9])) # "9534330"