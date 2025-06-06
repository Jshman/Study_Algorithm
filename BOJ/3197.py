from collections import deque

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

grid = []
days = []  # grid 정보를 담을 2차원 배열
parent = []
memo_q = deque()
column = -1

def make_index(y, x):
    return y * column + x


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(swan, els):
    swan_root = find(swan)
    els_root = find(els)
    if els_root == swan_root: return False
    parent[els_root] = swan_root
    return True


def bfs(i, j):
    q = deque()
    q.append((i, j))
    swan = make_index(i, j)

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if ny < 0 or ny >= r or nx < 0 or nx >= column or grid[ny][nx] == 'X':
                continue
            if union(swan, ny * column + nx):
                q.append((ny, nx))


def delete_ice(i, j):
    grid[i][j] = '.'

    for d in range(4):
        ny, nx = i + dy[d], j + dx[d]
        if ny < 0 or ny >= r or nx < 0 or nx >= column: continue
        if grid[ny][nx] in [',', 'L']:
            union(make_index(i,j), make_index(ny,nx))
            continue
        memo_q.append((ny, nx))

if __name__ == "__main__":
    r, c = map(int, input().split())
    column = c

    for _ in range(r):
        grid.append(list(input()))
        days.append(list(0 for _ in range(c)))
    parent = [i for i in range(r * c)]

    swans = []

    for i in range(r):
        for j in range(c):
            elem = grid[i][j]
            days[i][j] = 0
            if elem == 'X':
                for d in range(4):
                    ny, nx = i+dy[d], j+dx[d]
                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if grid[ny][nx] == '.':
                        memo_q.append((i,j))
                        break
                days[i][j] = 1
            if elem == 'L':  # 총 2번
                swans.append(make_index(i, j))
                bfs(i, j)

    day = 0
    # while find(swans[0]) != find(swans[1]):
    while day <= 10:
        day += 1
        for _ in range(len(memo_q)):
            y, x = memo_q.popleft()
            delete_ice(y, x)
        for e in grid:
            print(e)
        print(parent)

    print(day)