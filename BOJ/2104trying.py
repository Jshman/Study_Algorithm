# 2104 부분배열 고르기

N = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

tree = [0] *(N*4)

def init(start, end, idx=1):
    if start == end:
        tree[idx] = arr[end]
        return tree[idx]
    mid = (start+end) // 2
    tree[idx] = min(init(start,mid,idx*2), init(mid+1,end,idx*2+1))
    return tree[idx]

def interval(start, end, idx, left, right):
    if end < left or right < start:
        return float('inf')
    if left<=start and end<=right:
        return tree[idx]
    mid = (start+end)//2
    return min(interval(start, mid, idx*2, left, right), interval(mid+1, end, idx*2+1, left, right))

init(0, N-1)

for i in range()
