# 1976 여행 가자

# init
parent = []

def union(a, b):
    root_a = find_set(a)
    root_b = find_set(b)
    if root_a != root_b:
        parent[root_b] = root_a

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

if "__main__" == __name__:
    n = int(input())
    m = int(input())
    parent = [i for i in range(n)]

    for i in range(n):
        info = list(map(int, input().split()))
        for j in info:
            if info[j] == 0: continue
            union(i, j)
    print(parent)

    trip = list(map(int, input().split()))
    for i in range(1, m):
        if i >= n : continue
        if find_set(trip[i-1]-1) != find_set(trip[i]-1):
            print("NO")
            break
    else:
        print("YES")