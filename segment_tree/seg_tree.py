# 세그먼트 트리

arr = [i for i in range(1, 11)]
print(arr)

tree = [0] * (len(arr) * 4)

def init_tree(start, end, current):
    if (start == end):
        tree[current] = arr[start]
        return tree[current]
    
    mid = (start + end) // 2
    tree[current] = init_tree(start, mid, current*2) + init_tree(mid+1, end, current*2+1)
    return tree[current]

init_tree(0, len(arr)-1, 1)
print(tree)

# 내가 구현한 부분합 구하는 함수수
def sol(start, end, idx, i, k):
    if (i == k and start == end):
        return tree[idx]
    
    elif (start == i and end == k):
        return tree[idx]
    
    elif ((start > i and end < k) or (i > k)):
        return 0

    mid = (start + end) // 2
    return sol(start, mid, idx*2, max(start, i), min(mid, k)) + sol(mid+1, end, idx*2 +1, max(mid+1, i), min(end,k))
print(f"4 ~ 7까지 부분합:", sol(0, len(arr)-1, 1, 4, 7))


# 외부 사이트에서 구현되어 있는 부분합 함수
def interval(start, end, idx, i, j):
    if (i<=start and end<=j):
        return tree[idx]
    
    elif (end < i or start > j):
        return 0
    
    mid = (start+end) //2
    return interval(start, mid, idx*2, i, j) + interval(mid+1, end, idx*2 +1, i, j)

print(f"4 ~ 7까지 부분합:", interval(0, len(arr)-1, 1, 4, 7))

# idx: tree의 index위치
# where: arr에서 수정하는 위치
# value: 수정하는 값
def modify(start, end, idx, where, value):
    # 범위 바깥으로 나가면 종료
    if (where < start or where > end):
        return
    
    # 수정
    tree[idx] -= value
    # print(f"here-> {idx} {tree[idx]} {start} {end}")
    # 리프노드 까지 왔으면 종료
    if (start == end):
        return
    
    mid = (start+end) //2
    modify(start, mid, idx*2, where, value)
    modify(mid+1, end, idx*2+1, where, value)    
    
# arr[6] == 7
# 나는 100로 수정할 거임.
idx = 6
value = arr[idx] - 100  #=-93
print("수정할 값: ",value)
modify(0, len(arr)-1, 1, idx, value)

print(f"modify 이후 트리:",tree)

print(f"modify를 하고나서 4 ~ 7까지 부분합:", interval(0, len(arr)-1, 1, 4, 7))

