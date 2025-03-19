# 17404 RGB거리 2

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp=[[(float('inf'), 0) for _ in range(3)] for __ in range(n+1)]
for i in range(3):
    dp[0][i] = (0, i)

for i in range(1, n+1):
    for color in range(3):
        if i == n:
            if dp[n-1][0][1] == 0: #red
                dp[n][0] = min(dp[i-1][1:]) + min(rgb[i-1][1:])
            elif dp[n-1][1][1] == 1: #green
                dp[n][1] = min(dp[i-1][0], dp[i-1][2]) + min(rgb[i-1][0], rgb[i-1][2])
            else:
                dp[n][2] = min(dp[i-1][:2]) + min(rgb[i-1][:2])
            continue

        if color == 0:
            dp[i][color] = min(dp[i][color], min(dp[i-1][1:]) + rgb[i-1][color])
        elif color == 1:
            dp[i][color] = min(dp[i][color], dp[i-1][0] + rgb[i-1][color], dp[i-1][2] + rgb[i-1][color])
        else:
            dp[i][color] = min(dp[i][color], min(dp[i-1][:2]) + rgb[i-1][color])

for elem in dp:
    print(elem)