T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0] * (n+1) for _ in range(2)]
    
    scores = [list(map(int, input().split())) for _ in range(2)]
    
    
    for j in range(n):
        for i in range(2):
            if j > 1:
                dp[i][j] = max(dp[i-1][j-2], dp[i][j-2])
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]) + scores[i][j]
    
    ans = 0
    for elem in dp:
        ans = max(ans, max(elem))
    print(ans)