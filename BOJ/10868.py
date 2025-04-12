# 10868 최솟값
import sys
input = sys.stdin.readline

def init(start, end, idx=1):
    if start == end:
        tree[idx] = arr[end]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = min(init(start, mid, idx*2), init(mid+1, end, idx*2+1))
    return tree[idx]

def interval(start, end, idx, left, right):
    #범위 바깥
    if end < left or right < start:
        return float('inf')
    # 범위 안
    if left <= start and end <= right:
        return tree[idx]
    
    # 범위에 걸칠 때
    mid = (start+end)//2
    return min(interval(start,mid,idx*2,left,right), interval(mid+1,end,idx*2+1,left,right))

if __name__ == '__main__':
    N, M = map(int,input().split())
    arr = [int(input()) for _ in range(N)]
    
    tree = [0] * (N*4)
    init(0, N-1)

    for _ in range(M):
        a, b = map(int, input().split())
        print(interval(0, N-1, 1, a-1, b-1))