# 1717 집합의 연산
parent = [-1] * 1_000_001

def init_set(n):
    for i in range(n+1):
        parent[i] = i

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x]) #경로압축
    return parent[x]

def union(a, b):
    a_root = find_set(a)
    b_root = find_set(b)
    if a_root != b_root:
        parent[b_root] = a_root

if "__main__" == __name__:
    n, m = map(int, input().split())
    init_set(n)

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(a, b)    
        else:
            # a와 b가 같은 집합에 포함되어 있는지 확인하기
            print("YES" if find_set(a) == find_set(b) else "NO")