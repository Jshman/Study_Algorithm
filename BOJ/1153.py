# 1153 네 개의 소수

n = int(input())

prime = [True] * n
for i in range(2, n):
    if prime[i]:
        for j in range(i+i, n, i):
            prime[j] = False
prime_nums = [i for i in range(2, n) if prime[i]]


