A = input()
B = input()

dp = [['']*(len(A)+1) for _ in range(len(B)+1)]

for i in range(len(B)):
    for j in range(len(A)):
        if A[j] != B[i]:
            if len(dp[i][j]) < len(dp[i-1][j]):
                dp[i][j] = dp[i-1][j]
            if len(dp[i][j]) < len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
        else:
            if dp[i][j] == '':
                dp[i][j] = A[j]

            if len(dp[i][j]) < len(dp[i-1][j-1]) + 1:
                dp[i][j] = dp[i-1][j-1] + A[j]
print(len(dp[len(B)-1][len(A)-1]))
print(dp[len(B)-1][len(A)-1])