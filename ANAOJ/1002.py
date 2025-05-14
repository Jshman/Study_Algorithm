# 비밀 문자열

S = input()
T = list(input())
T.reverse()

for i in range(len(S)):
    if T != [] and T[-1] == S[i]:
        T.pop()
print("NO" if T else "YES")