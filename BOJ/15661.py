# 못 풀었음음

import math
from collections import deque

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
ans = float('inf')


def bfs(start, people, scoreA, scoreB):
    global ans
    queue = deque([start])

    if people == math.floor(N/2): #내림
        ans = min(ans, abs(scoreA-scoreB))
        return
    
    visited[start] = True

    while queue:
        cur = queue.popleft()
        for u, w in g[cur]:
            if not visited[u] and w > 1:
                score = w + 

    visited[start] = False