from collections import deque
def solution(s):
    answer = True
    if s[0] ==")" or s[-1] =="(":
        return False
    
    dq = deque(s)
    
    stack = [dq.popleft()]

    while dq:
        check = dq.popleft()
        if check == "(":
            stack.append(check)
        elif check == ")":
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    return True


print(solution("()()")) #true
print(solution("(())()")) #true
print(solution(")()(")) #true
print(solution("(()(")) #true