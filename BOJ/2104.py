# 2104 부분배열 고르기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def init(start, end, idx=1):
    if start == end:
        tree[idx] = (arr[end], end)
        return tree[idx] #value, index
    mid = (start+end) // 2
    tree[idx] = min(init(start,mid,idx*2), init(mid+1,end,idx*2+1))
    return tree[idx]

def interval(start, end, idx, left, right):
    if end < left or right < start:
        return (float('inf'), -1)
    if left<=start and end<=right:
        return tree[idx]
    
    mid = (start+end)//2
    l = interval(start, mid, idx*2, left, right)
    r = interval(mid+1, end, idx*2+1, left, right)
    if l[0] <= r[0]:
        return l
    return r

#0, N-1
def dc(l, r):
    if l > r:
        return 0

    min_val, min_idx = interval(0, N-1, 1, l, r)
    sum_of_range = prefix[r+1]-prefix[l]
    
    l_side = dc(l, min_idx-1)
    r_side = dc(min_idx+1, r)
    
    return max(sum_of_range * min_val, l_side, r_side)

if __name__=='__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    
    prefix = [0] * (N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + arr[i]

    tree = [0] *(N*4)
    init(0, N-1)
    
    ans = dc(0, N-1)
    print(ans)