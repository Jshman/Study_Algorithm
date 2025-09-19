# 1162 도로포장
from heapq import heappop, heappush
INF = float('inf')

N, M, K = map(int, input().split())

dist = [[INF for _ in range(N+1)] for __ in range(K+1)]
for k in range(K+1):
    dist[k][1] = 0 # 시작 노드는 비용 0

graph = {}
for _ in range(M):
    u, v, e = map(int, input().split())
    if u not in graph:
        graph[u] = [(v,e)]
    else:
        graph[u] += [(v, e)]
    
    if v not in graph:
        graph[v] = [(u, e)]
    else:
        graph[v] += [(u, e)]

pq = []
# 비용, 정점, 도로포장 횟수
heappush(pq, (0, 1, 0))
while pq:
    now_cst, now_vtx, wrapped = heappop(pq)
    if now_vtx not in graph: continue
    if dist[wrapped][now_vtx] < now_cst : continue #이미 구한 거리가 더 짧으면 무시한다.

    for nxt_v, nxt_c in graph[now_vtx]:
        expected_c = nxt_c + dist[wrapped][now_vtx]

        if expected_c < dist[wrapped][nxt_v]:
            dist[wrapped][nxt_v] = expected_c
            heappush(pq, (dist[wrapped][nxt_v], nxt_v, wrapped))
        
        if wrapped < K and dist[wrapped][now_vtx] + 0 < dist[wrapped+1][nxt_v]:
            dist[wrapped+1][nxt_v] = dist[wrapped][now_vtx] + 0
            heappush(pq, (dist[wrapped+1][nxt_v], nxt_v, wrapped + 1))

ans = INF
for elem in dist:
    ans = min(ans, elem[N])
print(ans)