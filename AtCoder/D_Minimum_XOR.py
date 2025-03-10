# 재귀를 이용한 풀이

N, M = map(int, input().split())
graph = [[-1 for _ in range(N+1)] for __ in range(N+1)]

for _ in range(M):
    u, v, e = map(int, input().split())
    graph[u][v] = e
    graph[v][u] = e

ans = float('inf')
visited = [False] * (1+N)

def dfs(cur_v, cur_e):
    global ans
    visited[cur_v] = True

    if cur_v == N:
        ans = min(ans, cur_e)
    
    for next_v in range(1, N+1):
        next_c = graph[cur_v][next_v]
        if next_c >= 0 and not (visited[next_v]):
            dfs(next_v, cur_e ^ next_c)
    visited[cur_v] = False
dfs(1, 0)
print(ans)