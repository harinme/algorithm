import sys
sys.stdin = open('./input/5250.txt')

def dp(matrix):
    dp = [[0] * size for _ in range(size)]

    dp[0][0] = 0
    for i in range(1, size):
        diff =  matrix[0][i] - matrix[0][i-1]
        dp[0][i] = dp[0][i-1] + 1 + (diff if diff > 0 else 0)
    for i in range(1, size):
        diff = matrix[i][0] - matrix[i-1][0]
        dp[i][0] = dp[i-1][0] + 1 + (diff if diff > 0 else 0)
    
    for i in range(1, size):
        for j in range(1, size):
            up_diff =  matrix[i][j] - matrix[i-1][j]
            up = dp[i-1][j] +  1  + (up_diff if up_diff > 0 else 0)
            left_diff = matrix[i][j] - matrix[i][j-1]
            left = dp[i][j-1] + 1 + (left_diff if left_diff > 0 else 0)

            dp[i][j] = min(up, left)
    
    return dp[size -1][size -1]


t = int(input())
for tc in range(1, t+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
  
    result = dp(matrix)

    print(f'#{tc} {result}')