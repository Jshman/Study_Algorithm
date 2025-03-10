N, M = map(int,input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1

    g[x].append((y, z))
    g[y].append((x, z))

