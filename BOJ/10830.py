# 10830

N, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

I = [[0]*N for _ in range(N)]
for i in range(N):
    I[i][i] = 1

def square(mat, n):
    if n == 1:
        return matrix_multiplication(mat, I)
    elif n%2 == 0:
        return square(matrix_multiplication(mat, mat), n//2)
    else:
        return matrix_multiplication(mat, square(matrix_multiplication(mat, mat), (n-1)//2))

def matrix_multiplication(A, B, mod=1000):
    ln = len(A)
    C = [[0]*ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            for k in range(ln):
                C[i][j] += (A[i][k] * B[k][j]) % mod
            C[i][j] %= mod
    return C
result = square(matrix, b)
for elm in result:
    print(*elm)
