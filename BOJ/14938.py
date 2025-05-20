# 14938 서강그라운드
from heapq import heappop, heappush

n, boundary, r = map(int, input().split())
items = list(map(int, input().split()))

graph = {}
for _ in range(r):
    a, b, l = map(int, input().split())
    if a not in graph:
        graph[a] = [(b, l)]
    else: graph[a] += [(b,l)]
    if b not in graph:
        graph[b] = [(a, l)]
    else: graph[b] += [(a,l)]

INF = float('inf')
ans = 0 # 얻을 수 있는 최대 아이템 개수
for i in range(n):
    dist = [INF] * (n+1)
    dist[i+1] = 0
    pq = []
    item = 0
    # 거리, 정점
    heappush(pq, (0, i+1))
    while pq:
        now_cost, now_ver = heappop(pq)
        if now_ver not in graph: continue
        if dist[now_ver] < now_cost: continue

        for next_ver, next_cost in graph[now_ver]: #현재 위치에서 갈 수 있는 모든 경로 탐색
            pay = dist[now_ver] + next_cost
            if pay < dist[next_ver]:
                dist[next_ver] = pay
                heappush(pq, (pay, next_ver))
    for j in range(n+1):
        if dist[j] <= boundary:
            item += items[j-1]
    ans = max(ans, item)
print(ans)