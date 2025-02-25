#7453 합이 0인 네 정수
n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A += [a]
    B += [b]
    C += [c]
    D += [d]

# 모든 A[a]+B[b] 합을 담을 AB 배열과 CD배열
AB = []
CD = []

for a in A:
    for b in B:
        AB.append(a + b)
for c in C:
    for d in D:
        CD.append(c + d)

# AB[i] + CD[j] = 0 은
# AB[i] = -CD[j] 이므로
# CD에 AB[i] * -1 이 있는지 확인만 하면 된다.
# 딕셔너리는 in 연산이 O(1) 인 점에서 AB[i] * -1 접근속도에 장점이 있다. 그래서 딕셔너리를 사용한다.
dict_ab = {}
for key in AB:
    key *= -1
    if key not in dict_ab:
        dict_ab[key] = 1
    else:
        dict_ab[key] += 1

answer = 0
for n in CD:
    if n in dict_ab:
        answer += dict_ab[n]
print(answer)