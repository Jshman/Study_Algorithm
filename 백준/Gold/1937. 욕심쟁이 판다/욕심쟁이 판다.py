import sys
sys.setrecursionlimit(10**6)

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dxys = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x):
    if dp[y][x] > 0:
        return dp[y][x]
    
    dp[y][x] = 1
    for dy, dx in dxys:
        ny, nx = y+dy, x+dx
        if not (0<=ny<n and 0<=nx<n) or grid[ny][nx] <= grid[y][x]:
            continue
    
        if dp[ny][nx] > 0:
            dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)
        else:
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
                
    return dp[y][x]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)