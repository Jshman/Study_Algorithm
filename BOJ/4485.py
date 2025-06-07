#4485 녹색 옷 입은 애가 젤다지?
from heapq import heappop, heappush

INF = float('inf')

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

def get_index(y, x, N):
    return N*y+x

if __name__ == '__main__':
    k = 0
    while (N:=int(input())) > 0:
        k+=1
        grid = [list(map(int, input().split())) for _ in range(N)]
        dist = [INF] * (N*N)

        pq = []
        heappush(pq, (grid[0][0], 0, 0))
        dist[0] = grid[0][0]
        while pq:
            lupi, y, x = heappop(pq)
            if lupi > dist[get_index(y, x, N)]: continue

            for d in range(4):
                ny, nx = y+dy[d], x+dx[d]
                if 0>ny or ny>=N or 0>nx or nx>=N:
                    continue
                
                pay = grid[ny][nx] + dist[get_index(y, x, N)]
                if pay < dist[get_index(ny, nx, N)] :
                    dist[get_index(ny, nx, N)] = pay
                    heappush(pq, (pay, ny, nx))

        print(f"Problem {k}: {dist[N*N-1]}")