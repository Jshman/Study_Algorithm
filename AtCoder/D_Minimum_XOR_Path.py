# stack
N, M = map(int, input().split())
graph = [[-1 for _ in range(N+1)] for __ in range(N+1)]

for _ in range(M):
    u, v, e = map(int, input().split())
    graph[u][v] = e
    graph[v][u] = e

start = 1
cost = 0

ans = float('inf')
stack = [(start, cost)]
visited = [False] * (N+1)  # 방문 체크 배열

while stack:
    current_node, current_cost = stack.pop()

    if current_node == N:
        ans = min(ans, current_cost)
        continue

    visited[current_node] = True

    for next_node in range(1, N+1):
        if graph[current_node][next_node] >= 0 and not visited[next_node]:
            stack.append((next_node, current_cost ^ graph[current_node][next_node]))

            graph[current_node][next_node] = -1 # -> 한 번 갔던 경로는 다시는 안 감.
            graph[next_node][current_node] = -1 # 더 효율적인 길이 있어도 이미 체크가 되었기 때문에 못 감.

    visited[current_node] = False
print(ans)