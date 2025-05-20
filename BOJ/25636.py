# 우선 최단경로를 구한다
# 최단경로를 역추적하면서 가장 많은 물을 얻는 길을 알아낸다.
# 최단경로는 평소와 같이 구하되, 업데이트 조건에 물의 양도 조건으로 추가해볼까?

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
water = list(map(int, input().split()))
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v, e = map(int, input().split())
    graph[u].append((v, e)) #정점, 비용
    graph[v].append((u, e))

S, T = map(int, input().split())

INF = float('inf')

dist = [INF] * (N+1) # 거리에 대한 table
dist[S] = 0 #출발지역의 비용은 0
water_gained = [0] * (N+1)  # 물에 대한 table
water_gained[S] = water[S-1] #충전됨

pq = []
heappush(pq, (0, S)) # 비용, 정점
while pq:
    cst, vtx = heappop(pq)
    if dist[vtx] < cst: continue #이미 갱신한 곳은 돌지 않음
    for next_vtx, move_cst in graph[vtx]:
        pay = move_cst + dist[vtx]
        if pay < dist[next_vtx]:
            #비용, 물
            dist[next_vtx] = pay
            water_gained[next_vtx] = water_gained[vtx] + water[next_vtx-1]
            heappush(pq, (pay, next_vtx))  # 비용, 정점

        elif pay == dist[next_vtx]:
            # 같으면 물을 더 많이 받을 수 있는지 확인하고 바꿔줌
            origin = water_gained[next_vtx]
            change = water_gained[vtx] + water[next_vtx-1]
            if origin == change : continue
            water_gained[next_vtx] = max(origin, change)
            heappush(pq, (pay, next_vtx))  # 비용, 정점
print(-1 if dist[T] == INF else f"{dist[T]} {water_gained[T]}")
