n, k = map(int, input().split())
coins=[]
for _ in range(n):
    coins+=[int(input())]
coins.sort()

dp = [0] * (k+1)
dp[0] = 1
for c in coins:
    for i in range(c, len(dp)):
        dp[i] += dp[i-c]

print(dp[k])