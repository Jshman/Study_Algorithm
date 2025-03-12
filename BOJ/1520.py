# 1520 내리막길
import sys
sys.setrecursionlimit(10**5)

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

#북 동 남 서
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
dp = [[-1]*c for _ in range(r)]

def DFS(y, x):
    if y == r-1 and x == c-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<r and 0<=nx<c and grid[ny][nx] < grid[y][x]:
            dp[y][x] += DFS(ny, nx)
    return dp[y][x]
    
print(DFS(0, 0))