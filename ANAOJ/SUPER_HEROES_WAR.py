import heapq, sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, lvl = map(int, input().split()) #몬스터 수, 현석이 레벨
    tmp = list(map(int, input().split()))
    arr = []
    for monster in tmp:
        heapq.heappush(arr, monster)

    can = True
    while arr:
        monster = heapq.heappop(arr)
        if monster < lvl:
            lvl += monster
        else:
            if monster == lvl and len(arr)==0:
                break
            else:
                can = False
    print("YES" if can else "NO")