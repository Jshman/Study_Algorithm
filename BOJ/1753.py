# 1753 최소비용

import heapq

V, E = map(int, input().split())
dist = [float('inf')] * (V+1)

start_V = int(input())
dist[start_V] = 0

# [start][to]에 가면 (정점, 코스트)
# graph = [[(-1, -1) for _ in range(V+1)] for __ in range(V+1)]
graph = {}
for _ in range(E):
    u, v, e = map(int, input().split())
    if u not in graph:
        graph[u] = [(v, e)]
    else:
        graph[u] += [(v, e)]
print(graph)
pq = []
# cost, 정점
heapq.heappush(pq, (0, start_V))
while pq :
    cst, vtx = heapq.heappop(pq)
    if (vtx not in graph) : continue
    for nxt_vtx, nxt_cst in graph[vtx]:
        if nxt_cst + dist[vtx] < dist[nxt_vtx]:
            dist[nxt_vtx] = nxt_cst + dist[vtx]
            heapq.heappush(pq, (dist[nxt_vtx], nxt_vtx))
    
for i in dist[1:]:
    print(i if i!=float('inf') else "INF")