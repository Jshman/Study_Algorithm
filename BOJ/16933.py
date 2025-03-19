# 벽 부수고 이동하기3
from collections import deque

n, m, k = map(int, input().split())
mz = [input() for _ in range(n)]
q = deque()
visited = [[[False for _ in range(m)] for __ in range(n)] for ___ in range(k+1)]

# 남동북서
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

# y, x, dim, move
start = (0, 0, 0, 1)
apd = q.append
apd(start)
while q:
    v = 0
    y, x, dim, move = q.popleft()

    if y==n-1 and x == m-1:
        print(move)
        break

    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if not (0<=ny<n and 0<=nx<m) : continue
        if not visited[dim][ny][nx]:
            if mz[ny][nx]=='1':
                if dim<k: v = 1
                else: continue
            move_to = (ny, nx, dim+v, move+1)
            v=0
            visited[dim][ny][nx] = True
            apd(move_to)
else:
    print(-1)