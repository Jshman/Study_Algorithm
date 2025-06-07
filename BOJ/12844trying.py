#12844 XOR
import sys
input = sys.stdin.readline

def init(start, end, idx=1):
    if start==end:
        tree[idx] = arr[end]
        return tree[idx]
    mid = (start + end)//2
    tree[idx] = init(start,mid,idx*2) ^ init(mid+1, end, idx*2+1)
    return tree[idx]

def push_lazy(start, end, idx):
    if lazy[idx] != 0: 
        if (end - start + 1) % 2 == 1:
            tree[idx] ^= lazy[idx]


        if start != end:
            lazy[idx*2] ^= lazy[idx]
            lazy[idx*2+1] ^= lazy[idx]

        lazy[idx] = 0

def interval(start, end, idx, left, right):
    push_lazy(start, end, idx)
    if end < left or right < start:
        return 0
    
    if left<=start and end<=right:
        return tree[idx]
    
    mid = (start+end)//2
    return interval(start, mid, idx*2, left, right) ^ interval(mid+1, end, idx*2+1, left, right)

def modify(start, end, idx, left, right, k):
    push_lazy(start, end, idx)
    if end < left or right < start:
        return tree[idx]
    
    if left <= start and end <= right:
        lazy[idx] ^= k
        push_lazy(start, end, idx)
        return tree[idx]
    
    mid = (start+end)//2
    tree[idx] = modify(start, mid, idx*2, left, right, k) ^ modify(mid+1, end, idx*2+1, left, right, k)
    return tree[idx]
    
if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (n*4)
    lazy = [0] * (n*4)
    init(0, n-1)

    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            i, j, k = query[1:]
            modify(0, n-1, 1, i-1, j-1, k)
        else:
            i, j = query[1:]
            print(interval(0, n-1, 1, i-1, j-1))
