N, M=map(int,input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort()
W.sort()

ans = 0
canUseWhite = 0

while B:
    blackBall = B.pop()
    canUseWhite += 1

    if blackBall >= 0:
        ans += blackBall
        if len(W) >0 and (whiteBall:=W[-1]) >= 0:
            if len(W) == 0:
                continue
            ans += W.pop()
            canUseWhite -= 1

    if blackBall < 0:
        if len(W) == 0:
            continue
        whiteBall = W[-1]
        if blackBall + whiteBall >= 0 and canUseWhite > 0:
            ans += blackBall + whiteBall
            W.pop()
            canUseWhite -= 1

print(ans)