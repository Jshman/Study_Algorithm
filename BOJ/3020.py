# 3020 개똥벌레_누적합
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

# 종유석에 대한 누적합 (이 이상에서 벽을 뚫는다.)
prefix = [0] * (H+1)
for elem in stalactites:
    prefix[elem] += 1
for i in range(H):
    prefix[i+1] += prefix[i]


# 석순에 대한 누적합 (이 이하에서 벽을 뚫는다.)
prefix_reverse = [0] * (H+1)
for elem in stalagmites:
    prefix_reverse[elem] += 1
prefix_reverse.reverse()

for i in range(H):
    prefix_reverse[i+1] += prefix_reverse[i]
prefix_reverse.reverse()

# 정답 구하기
m, cnt = 10**7, 0

for i in range(1, H+1):
    if prefix[i] + prefix_reverse[i] < m:
        cnt = 1
        m = prefix[i] + prefix_reverse[i]
    elif prefix[i] + prefix_reverse[i] == m:
        cnt += 1
print(m, cnt)