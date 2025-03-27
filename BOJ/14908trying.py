#구두 수선공

n=int(input())
inp = []
works = []
for _ in range(n):
    t,s = map(int, input().split())
    inp += [(t,s,0)]
    works += [(t,s,0)]

ssum = sum(x[1] for x in inp)
used = set()
sequence = []
total = 0

for i in range(n):
    tmp = ssum
    mini = float('inf')
    mini_idx = -1

    for j in range(n):
        if j in used:
            continue
        tmp = (ssum - inp[j][1]) * inp[j][0]
        if tmp < mini:
            mini = tmp
            mini_idx = j

    used.add(mini_idx)
    sequence.append(mini_idx+1)
    ssum -= inp[mini_idx][1]

for idx in sequence:
    print(idx, end=" ")
