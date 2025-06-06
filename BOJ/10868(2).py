# 희소배열

N, M = map(int, input().split())
dp = [[None for __ in range(N)] for _ in range(25)]
for j in range(N):
    dp[0][j] = j


for i in range(1, 25):
    for j in range(N):
        print("i j:",i, j)
        dp[i][j] = dp[i-1][dp[i-1][j]]
    print(dp[i])

for _ in range(M):
    L, R = map(int, input().split())
    