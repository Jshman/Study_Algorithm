# 6549 히스토그램에서 가장 큰 직사각형
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def init(start, end, idx=1):
    if start == end:
        tree[idx] = (arr[end], end)
        return tree[idx]
    mid = (start+end)//2
    left = init(start,mid,idx*2)
    right = init(mid+1,end,idx*2+1)
    
    tree[idx] = min(left, right)
    return tree[idx]

def interval(start, end, idx, left, right):
    if right < start or end < left:
        return (float('inf'), float('inf'))
    
    if left<=start and end<=right:
        return tree[idx]
    
    mid=(start+end)//2

    i = interval(start,mid,idx*2,left,right)
    j = interval(mid+1,end,idx*2+1,left,right)
    return min(i, j)

def sol(l, r):
    if l == r:
        return arr[r]
    elif l > r:
        return 0
    min_val, min_idx = interval(1, len(arr)-1, 1, l, r)
    area = min_val * (r-l+1)

    a1 = sol(l, min_idx-1) # l == r 가능
    a2 = sol(min_idx+1, r) # l > r 가능
    return max(area, a1, a2, arr[min_idx])

answers=[]
while 1:
    arr = list(map(int,input().split()))
    if len(arr)==1 and arr[0]==0:
        break
    tree = [0] * (len(arr)*4)
    init(1, len(arr)-1)

    min_idx = 10**6
    min_val = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    
    ans = sol(1, len(arr)-1)
    print(ans)
    answers.append(ans)
print(answers)