# 1966 프린터 큐
from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    importance = max(arr) # 중요도
    dq = deque()
    for i in range(N):
        dq.append((arr[i], i)) #중요도, 순서
    cnt = 0 # 출력한 횟수
    while dq:
        impt, order = dq.popleft()
        if impt < importance:
            dq.append((impt, order))
            continue
        else:
            cnt+=1
            if order == M:
                print(cnt)
                break
            arr[order] = 0
            importance = max(arr)