#1937 욕심쟁이 판다
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#북동남서
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
dp = [[1 for _ in range(n)] for __ in range(n)]
        
ans = 0
for i in range(n):
    for j in range(n):
        stack = [(i, j, 1)]
        ret = 0
        while stack:
            y, x, depth = stack.pop()
            # print(y, x, depth, grid[y][x])
            ret = max(ret, depth)

            for d in range(4):
                ny, nx = y+dy[d], x+dx[d]
                if not (0<=ny<n and 0<=nx<n):
                    continue
                if grid[y][x] < grid[ny][nx]:
                    stack.append((ny, nx, depth + 1))
        dp[i][j] = ret
        ans = max(ans, ret)
        
print(ans)