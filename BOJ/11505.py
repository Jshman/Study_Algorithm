# 11505 구간 곱 구하기
import sys
input = sys.stdin.readline

mod_value = 10**9+7

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N*4)

def init(start, end, idx=1):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end)//2
    tree[idx] = (init(start, mid, idx*2) * init(mid+1, end, idx*2+1)) % mod_value
    return tree[idx]

def interval(start, end, idx, left, right):
    # 범위 바깥
    if end < left or right < start:
        return 1
    # 범위 일치
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start+end) // 2
    return (interval(start, mid, idx*2, left,right) * interval(mid+1, end, idx*2+1,left,right)) % mod_value

def update(start, end, idx, where, new):
    # 범위 바깥
    if end < where or where < start:
        return tree[idx]
    # 말단 노드
    if start == end:
        tree[idx] = new
        return tree[idx]
    # 업데이트 거꾸로 올라오는 방법으로 구현 다시하기
    # 걸치는 구간은 재귀로 처리
    mid = (start + end) // 2
    tree[idx] = (update(start,mid,idx*2, where, new) * update(mid+1,end,idx*2+1, where, new)) % mod_value
    return tree[idx]

def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)  # 페르마 소정리로 역원 계산

def update2(start, end, idx, where, new):
    if end < where or where < start:
        return
    
    tree[idx] = ((tree[idx] // arr[where]) % mod_value * new) % mod_value

    if start == end:
        arr[where] = new
        return

    mid = (start + end) // 2
    update2(start, mid, idx*2, where, new)
    update2(mid+1, end, idx*2+1, where, new)


init(0, N-1)
repeat = M+K
for _ in range(repeat):
    a,b,c = map(int, input().split())
    if a == 1:
        if arr[b-1] % mod_value == 0:
            arr[b-1] = c
            init(0, N-1)
            continue
        update2(0, N-1, 1, b-1, c)
        arr[b-1] = c
    else:
        print(interval(0, N-1, 1, b-1, c-1) % mod_value)