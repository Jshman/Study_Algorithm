# 3020 개똥벌레_이분탐색
from bisect import bisect_left, bisect_right

N, H = map(int, input().split())

# 종유석, 석순
stalactites, stalagmites = [], []
for i in range(N):
    if i%2 == 0:
        stalagmites += [int(input())]
    else:
        stalactites += [int(input())]

# 종유석 전처리
for i in range(len(stalactites)):
    stalactites[i] = H - stalactites[i] + 1

# 종유석
stalactites.sort()
st = []
for h in range(1, H+1):
    st.append(bisect_right(stalactites, h))

# 석순
stalagmites.sort()
sm = []
for h in range(1, H+1):
    sm.append(len(stalagmites) - bisect_left(stalagmites, h))


# 정답 구하기
m, cnt = 10**7, 0
test = []
for i in range(H):
    test.append(st[i] + sm[i])
    if st[i] + sm[i] < m :
        cnt = 1
        m = st[i] + sm[i]
    elif st[i] + sm[i] == m:
        cnt += 1
print(m, cnt)