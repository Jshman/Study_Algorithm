N = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, (N-1)
ans = float('inf')
k1, k2 = -1, -1
while l<r:
    diff = arr[l] + arr[r]
    if abs(diff) < ans:
        k1, k2 = arr[l], arr[r]
        ans = abs(diff)
    if diff < 0 :
        l += 1
    elif diff > 0:
        r -= 1
    else:
        break

print(k1, k2)