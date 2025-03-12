# 15989 1,2,3 만들기 4 -fail
import math

t = set()
for a in range(100):
    for b in range(100):
        if 2**a * 3**b > 10**18: break
        t.add(2**a * 3**b)
t.remove(4)

dp = [0, 1, 2, 3]
for i in range(4,20):
    k = (dp[i-1]-dp[i-3]) / (1+(not i in t))
    if i in t:
        dp += [dp[i-1] + math.ceil(k)]
    else:
        dp += [dp[i-1] + math.floor(k)]

print(dp)
n=int(input())
for _ in range(n):
    print(dp[int(input())])
