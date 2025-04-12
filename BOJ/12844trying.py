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
        tree[idx] ^= lazy[idx]

        if start != end:
            lazy[idx*2] ^= lazy[idx]
            lazy[idx*2+1] ^= lazy[idx]
        lazy[idx] = 0

def interval(start, end, idx, left, right):
    push_lazy(start, end, idx)
    # 범위 안
    if left<=start and end<=right:
        return tree[idx]
    #범위 바깥
    if end < left or right < start:
        # 어떤 수든 0과 xor 연산을 하면 그 값을 유지함
        return 0
    mid = (start+end)//2
    return interval(start,mid,idx*2,left,right) ^ interval(mid+1,end,idx*2+1,left,right)

# xor 연산은 교환법칙이 성립한다.
def modify(start, end, idx, left, right, k):
    push_lazy(start, end, idx)
    #범위 바깥은 리턴
    if end < left or start > right:
        return
    if left<=start and end<=right:
        lazy[idx] ^= k
        push_lazy(start, end, idx)
        return
    if start == end:
        tree[idx]^=k
        return
    
    mid = (start + end)//2
    modify(start, mid, idx*2, left, right, k)
    modify(mid+1, end, idx*2+1, left, right, k)
    tree[idx] = tree[idx*2] ^ tree[idx*2+1]
    
if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (n*4);init(0, n-1)
    lazy = [0] * (n*4)
    print(tree)
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # arr[i~j]에 k를 xor 한다.
            i, j, k = query[1:]
            modify(0, n-1, 1, i, j, k)
        else:
            # arr[i~j]를 모두 xor한 다음 출력한다.
            i, j = query[1:]
            print(interval(0, n-1, 1, i, j))
    print(tree)
