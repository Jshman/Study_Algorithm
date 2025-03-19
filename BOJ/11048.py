#11048 이동하기

n, m = map(int, input().split())
mz = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for __ in range(n)]
dp[0][0] = mz[0][0]

# 남 동 남동
dy, dx = [1, 0, 1], [0, 1, 1]

for y in range(n):
    for x in range(m):
        for i in range(3):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                dp[ny][nx] = max(dp[ny][nx], dp[y][x] + mz[ny][nx])
print(dp[n-1][m-1])