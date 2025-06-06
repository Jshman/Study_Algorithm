import sys
sys.setrecursionlimit(10**9)

I = [[0]*2 for _ in range(2)]
for i in range(2):
    I[i][i] = 1

answers = []

def square(mat, n):
    if n == 1:
        return matrix_multiplication(mat, I)
    elif n%2 == 0:
        return square(matrix_multiplication(mat, mat), n//2)
    else:
        return matrix_multiplication(mat, square(matrix_multiplication(mat, mat), (n-1)//2))

def matrix_multiplication(A, B, mod=10**9+7):
    ln = len(A)
    C = [[0]*ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            for k in range(ln):
                C[i][j] += (A[i][k] * B[k][j]) % mod
            C[i][j] %= mod
    return C

def F(x):
    if x == 0:
        return 1
    ret = square([[0,1], [1,1]], x)[1][0] + square([[0,1], [1,1]], x-1)[1][0]
    for i in range(0, x):
        ret = (ret + ((square([[0,1], [1,1]], x)[1][0]) * c)) % (10**9+7)
    return ret

if __name__ == '__main__':
    c, k = map(int, input().split())
    answer = F(k)
    print(answer)