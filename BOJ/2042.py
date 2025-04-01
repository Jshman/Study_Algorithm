# 2042 구간 합 구하기
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N*4)

def init(start, end, idx):
    if(start == end):
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start+end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

def interval(start, end, idx, left, right):
    if (end < left or right < start):
        return 0;
    if (left <= start and end <= right):
        return tree[idx]
    mid = (start+end)//2
    return interval(start,mid,idx*2,left,right) + interval(mid+1, end, idx*2+1,left,right)

def modify(start, end, idx, where, value):
    if (where < start or end < where):
        return
    
    tree[idx] -= value

    if (start == end):
        return
    mid = (start+end) // 2
    modify(start, mid, idx*2, where, value)
    modify(mid+1, end, idx*2 +1, where, value)

init(0, N-1, 1)

repeat = M+K
for _ in range(repeat):
    a, b, c = list(map(int, input().split()))
    if (a == 1):
        modify(0, N-1, 1, b-1, arr[b-1] - c)
        arr[b-1] = c
    else:
        print(interval(0, N-1, 1, b-1, c-1))
