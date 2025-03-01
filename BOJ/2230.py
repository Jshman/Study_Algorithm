# 2230 수 고르기
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

l, r = 0, 0
ans = float('inf')

while l <= r and r < N:
    differ = abs(arr[r] - arr[l])
    if differ < M:
        r += 1
    elif differ >= M:
        l += 1
        ans = min(ans, differ)
print(ans)
