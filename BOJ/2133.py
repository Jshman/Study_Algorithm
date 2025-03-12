#2133 3*n 타일 채우기

dp = [1, 0, 3, 0]
for i in range(4,31):
    dp.append(0 if i%2 != 0 else (dp[i-2]*4-dp[i-4]))
print(dp[int(input())])
print(len(dp))