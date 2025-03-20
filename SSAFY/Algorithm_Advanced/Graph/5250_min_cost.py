import sys
sys.stdin = open('./input/5250.txt')

def dp(matrix):
    dp = [[0] * size for _ in range(size)]

    dp[0][0] = matrix[0][0]
    for i in range(1, size):
        dp[0][i] = dp[0][i-1] + abs(matrix[0][i] - matrix[0][i-1])
    for i in range(1, size):
        dp[i][0] = dp[i-1][0] + abs(matrix[i][0] - matrix[i-1][0])
    
    for i in range(1, size):
        for j in range(1, size):
            matrix
            # dp[i][j] = 
    


    return dp


t = int(input())
for tc in range(1, t+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
  



    print(dp(matrix))


    print(f'#{tc} ')