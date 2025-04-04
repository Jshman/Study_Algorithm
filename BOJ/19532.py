# 19532 수학은 비대면강의입니다
a,b,c,d,e,f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if c == (a*x + b*y) and f == (d*x + e*y):
            print(x, y)
            break
    else:
        continue
    break;