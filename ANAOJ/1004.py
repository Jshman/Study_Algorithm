N = int(input())
a= list(map(int, input().split()))
b= list(map(int, input().split()))

for i in range(N-1):
    a[i+1] += b[i] - a[i]
print("YES" if a[-1] == b[-1] else "NO")