from collections import deque

def solution(tickets):
    tickets.sort()
    que = deque()
    for i in range(len(tickets)):
        s, e = tickets[i]
        if s == "ICN":
            visited = [False] * len(tickets)
            visited[i] = True
            que.append((e, ["ICN", e], visited))

    
    while que:
        cur, path, visited = que.popleft()
        
        if len(path) == len(tickets) + 1:
            return path

        for i in range(len(tickets)):
            x, y = tickets[i]
            if x == cur and not visited[i]:
                new_visited = visited.copy()
                new_visited[i] = True
                que.append((y, path + [y], new_visited))

        que = deque(sorted(que, key=lambda x: x[1]))

       
        


    return path

# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))


# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))