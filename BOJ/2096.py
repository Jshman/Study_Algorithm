arr_min=[0,0,0]
arr_max=[0,0,0]

n=int(input())
for _ in range(n):
    inp=list(map(int,input().split()))
    tmp_min = [arr_min[0], arr_min[1], arr_min[2]]
    arr_min[0] = inp[0] + min(tmp_min[0], tmp_min[1])
    arr_min[1] = inp[1] + min(tmp_min)
    arr_min[2] = inp[2] + min(tmp_min[1], tmp_min[2])

    tmp_max = [arr_max[0], arr_max[1], arr_max[2]]
    arr_max[0] = inp[0] + max(tmp_max[0], tmp_max[1])
    arr_max[1] = inp[1] + max(tmp_max)
    arr_max[2] = inp[2] + max(tmp_max[1], tmp_max[2])

print(max(arr_max),min(arr_min))