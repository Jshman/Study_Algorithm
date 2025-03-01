N, H = map(int, input().split())

# 종유석 (천장에서 내려옴), 석순 (바닥에서 올라옴)
stalactites, stalagmites = [], []
for i in range(N):
    if i % 2 == 0:
        stalagmites.append(int(input()))  # 짝수 번째 입력 → 석순
    else:
        stalactites.append(int(input()))  # 홀수 번째 입력 → 종유석

# 종유석을 H 기준으로 변환 (높이 h 이상에서 부딪힘)
for i in range(len(stalactites)):
    stalactites[i] = H - stalactites[i] + 1

# 🔸 종유석(Stalactites) 누적합 배열 (h 이상에서 부딪힘)
stalactite_prefix_sum = [0] * (H + 1)
for height in stalactites:
    stalactite_prefix_sum[height] += 1
for i in range(1, H + 1):
    stalactite_prefix_sum[i] += stalactite_prefix_sum[i - 1]

# 🔸 석순(Stalagmites) 누적합 배열 (h 이하에서 부딪힘)
stalagmite_prefix_sum = [0] * (H + 1)
for height in stalagmites:
    stalagmite_prefix_sum[height] += 1

# 배열을 뒤집어서 "h 이하에서 부딪히는 개수"로 변환
stalagmite_prefix_sum.reverse()
for i in range(1, H + 1):
    stalagmite_prefix_sum[i] += stalagmite_prefix_sum[i - 1]
stalagmite_prefix_sum.reverse()  # 원래 순서로 되돌림

# 🔹 최소 장애물 개수 & 해당 구간 개수 찾기
min_obstacles = float('inf')
count = 0

for h in range(1, H + 1):
    obstacles = stalactite_prefix_sum[h] + stalagmite_prefix_sum[h]
    
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1  # 새로운 최소값 발견 시 초기화
    elif obstacles == min_obstacles:
        count += 1  # 같은 최소값이 나올 때마다 개수 증가

# 결과 출력
print(min_obstacles, count)
