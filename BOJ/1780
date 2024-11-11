# 1780 종이의 개수

k = int(input())
matrix = [list(map(int, input().split())) for _ in range(k)]
result = [0, 0, 0]  # 0, 1, -1 개수

def sol(n, r, c):
    color = matrix[r][c]
    if n == 1:
        result[color] += 1
        return

    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != matrix[i][j]:
                sol(n//3, r, c)
                sol(n//3, r, c + n//3)
                sol(n//3, r, c + 2*(n//3))

                sol(n//3, r + n//3, c)
                sol(n//3, r + n//3, c + n//3)
                sol(n//3, r + n//3, c + 2*(n//3))

                sol(n//3, r + 2*(n//3), c)
                sol(n//3, r + 2*(n//3), c + n//3)
                sol(n//3, r + 2*(n//3), c + 2*(n//3))
                return
    result[color] += 1

sol(k,0,0)
print(f"{result[-1]}\n{result[0]}\n{result[1]}")
