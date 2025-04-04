# 히스토그램에서 가장 큰 직사각형
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def init(start, end, idx=1):
    if start == end:
        tree[idx] = (arr[end], end)
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = min(init(start, mid, idx*2), init(mid+1, end, idx*2+1))
    return tree[idx]

def interval(start, end, idx, left, right):
    if left<=start and end<=right:
        return tree[idx]
    if end < left or right < start:
        return (float('inf'), float('inf'))
    mid = (start+end)//2
    i = interval(start,mid,idx*2,left,right)
    j = interval(mid+1,end,idx*2+1,left,right)
    
    # 메모리 오버헤드 방지
    # min 연산은 튜플 비교, 너무 많은 메모리를 사용케 됨.
    if i[0] <= j[0]:
        return i
    else:
        return j

def dc(left, right):
    if left>right:
        return 0 # min_idx == right 였던 경우에 조건문을 만족함. 범위 바깥으로 나가는 경우임
    elif left == right: 
        return interval(1, leng, 1, left, left) # left == min_idx-1 였던 경우에 만족함
    
    min_val, min_idx = interval(1, leng, 1, left, right)
    l_side = dc(left, min_idx-1)
    middle = min_val * (right - left + 1)
    r_side = dc(min_idx+1, right)

    return max(l_side, middle, r_side)

# N 보다 크거나 같은 제곱수 중 최솟값을 구하는 함수
def get(n):
    i = 2
    while 1:
        if n <= i**2: return i**2
        i+=1

while 1:
    # inputs[0] == 길이
    # inputs[1:] == array
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    leng = arr[0]
    tree = [0] * (get(leng))
    init(1, arr[0])
    arr = [] #arr 초기화
    ans = dc(1, leng)
    print(ans)
