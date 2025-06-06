from heapq import heappop, heappush
INF = float('inf')

N, M, T = map(int, input().split())

dist = [[INF for _ in range(N+1)] for __ in range(2)]
dist[0][1] = 0 # 시작 노드는 비용 0
# 여기 주의해서 [k][1] = 거울세계 비용 지불해야할수도있음 이부분

graph = {}
for _ in range(M):
    u, v, e = map(int, input().split())
    if u not in graph:
        graph[u] = [(v,e)]
    else:
        graph[u] += [(v, e)]

pq = []
# 비용, 정점, 도로포장 횟수
heappush(pq, (0, 1, 0))
while pq:
    now_cst, now_vtx, mirror = heappop(pq)
    if now_vtx not in graph: continue
    if dist[mirror][now_vtx] < now_cst : continue #이미 구한 거리가 더 짧으면 무시한다.

    for nxt_v, nxt_c in graph[now_vtx]:
        expected_c = nxt_c + dist[mirror][now_vtx]

        if expected_c < dist[mirror][nxt_v]:
            dist[mirror][nxt_v] = expected_c
            heappush(pq, (dist[mirror][nxt_v], nxt_v, mirror))
        
        if mirror < 1 and dist[mirror][now_vtx] + T < dist[mirror+1][nxt_v]:
            dist[mirror+1][nxt_v] = dist[mirror][now_vtx] + T
            heappush(pq, (dist[mirror+1][nxt_v], nxt_v, mirror + 1))

ans = INF
for elem in dist:
    ans = min(ans, elem[N])
print(ans if ans != INF else -1)