# 2589 보물섬
from collections import deque

def init_dist():
    return [[0 for _ in range(c)] for __ in range(r)]

r, c = map(int, input().split())
mp = [input() for _ in range(r)]
ans = 0
q = deque()
# 북, 서, 남, 동
directions = [(-1,0), (0,-1), (1,0), (0,1)]

for i in range(r):
    for j in range(c):
        if mp[i][j] == 'W':
            continue
        q.append((i,j))
distances = init_dist()

while q:
    y, x = q.popleft()
    if mp[y][x] == 'W':
        continue
    for d in directions:
        dy, dx = d
        ny, nx = y+dy, x+dx
        if 0<=ny and ny<r and 0<=nx and nx<c and mp[ny][nx]=="L":
            # 한 번도 방문한 적 없거나 기존 경로보다 더 적은 경로로 이동가능하다면
            if distances[ny][nx] == 0:
                distances[ny][nx] = distances[y][x] + 1
                q.append((ny,nx))
            elif distances[ny][nx] > 0:
                distances[ny][nx] = min(distances[y][x] + 1, distances[ny][nx])
                q.append((ny,nx))
            ans = max(ans, distances[ny][nx])

print(ans)