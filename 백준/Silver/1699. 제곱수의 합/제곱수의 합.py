n = int(input())+1
dp = [i for i in range(n)]
for i in range(n):
    m = int(i**0.5) + 1
    for j in range(1, m):
        dp[i] = min(dp[i], dp[i - (j**2)] + 1)
print(dp[n-1])