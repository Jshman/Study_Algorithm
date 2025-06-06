# 7469 K번째 수
import bisect

tree = []
arr = []

def merge(arr):
    if len(arr) < 2: return arr
    mid = len(arr)//2
    lo_arr = merge(arr[:mid])
    hi_arr = merge(arr[mid:])
    print(arr)
    merged_arr = []
    l,h = 0,0
    while l<len(lo_arr) and h<len(hi_arr):
        if lo_arr[l] < hi_arr[h]:
            merged_arr.append(lo_arr[l])
            l+=1
        else:
            merged_arr.append(hi_arr[h])
            h+=1
    merged_arr += lo_arr[l:]
    merged_arr += hi_arr[h:]
    print("merged",lo_arr, hi_arr)

    return merged_arr


def init_tree(start, end, idx=1):
    if start == end:
        tree[idx] = [arr[start]]
        return tree[idx]
    mid = (start + end) // 2
    non_sorted = init_tree(start, mid, idx * 2) + init_tree(mid + 1, end, idx * 2 + 1)
    tree[idx] = merge(non_sorted)
    
    return tree[idx]


def interval(start, end, left, right, idx=1):
    if end < left or right < start:
        return []

    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    ret = interval(start, mid, left, right, idx * 2) + interval(mid + 1, end, left, right, idx * 2 + 1)
    # ret.sort() #여기서 아니면, 밑에 main 함수에서 나온 값에서 sort해줌
    return ret

if __name__ == '__main__':
    n, m = map(int, input().split())
    inp = list(map(int, input().split()))
    for e in inp:
        arr.append(e)

    tree = [[] for _ in range(n * 4)]
    init_tree(0, n - 1)
    print(tree)
    # Query 처리
    for _ in range(m):
        left, right, k = map(int, input().split())
        interval_list = interval(0, n - 1, left - 1, right - 1)
        print(interval_list)
        print(interval_list[k-1])
    