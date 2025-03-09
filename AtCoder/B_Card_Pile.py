N=int(input())
lst=[0]*100
for _ in range(N):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        lst += [cmd[1]]
    else:
        n = lst.pop()
        print(n)
