# 1562 계단수
dp = [9, 17]
a = 0
for i in range(101):
    dp.append(dp[i-1] * 2 - 2)
print(sum(dp[:101])%10**9)