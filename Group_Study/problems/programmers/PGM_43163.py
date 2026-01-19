from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    word_len = len(begin)  # 단어의 길이
    
    def can_transform(word1, word2):
        diff_count = 0
        for i in range(word_len):
            if word1[i] != word2[i]:
                diff_count += 1
        return diff_count == 1
    
    def bfs():
        que = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
        visited = {begin}
        
        while que:
            cur, num = que.popleft()
            
            if cur == target:
                return num
            
            for word in words:
                if word not in visited and can_transform(cur, word):
                    visited.add(word)
                    que.append((word, num + 1))
        
        return 0
    
    return bfs()


# 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

# 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"] ))