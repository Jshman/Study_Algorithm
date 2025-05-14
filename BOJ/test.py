eight_num = 888_888_888_888_888_888
eights = [eight_num//(10**i) for i in range(18)]
# print(type(eights[0]))
t = int(input())
for _ in range(t):
    n = int(input())
    idx = 0
    while idx<19 and n>0:
        if n - eights[idx] < 0:
            idx+=1;
            continue
        n -= eights[idx]
    print("Yes")
    