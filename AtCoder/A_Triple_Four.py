N=int(input())
arr=list(map(int,input().split()))

cnt=1
num=arr[0]
ans="No"
for i in range(1,N):
    if num==arr[i]:
        cnt+=1
        if cnt >= 3:
            ans="Yes"
    else:
        num=arr[i]
        cnt=1
print(ans)