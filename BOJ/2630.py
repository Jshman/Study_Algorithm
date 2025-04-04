# 2630 색종이 만들기

N = int(input())
paper=[input().split() for _ in range(N)]

def sol(length, r=0, c=0, depth=0):
    if length == 1:
        if paper[r][c] == '1':
            return [0, 1]
        else:
            return [1, 0]
    
    pivot = paper[r][c]
    for i in range(r, r+length):
        for j in range(c, c+length):
            if paper[i][j] != pivot:       
                length //= 2
                w, b = sol(length, r, c, depth+1)
                x = sol(length, r + length, c, depth+1)
                y = sol(length, r, c + length, depth+1)
                z = sol(length, r + length, c + length, depth+1)
                w += x[0] + y[0] + z[0]
                b += x[1] + y[1] + z[1]
                return [w, b]
    if pivot == '1':
        return [0, 1]
    else:
        return [1, 0]

            
w,b = sol(N)
print(w,b,sep="\n")
