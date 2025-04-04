# 1629 곱셈

def power(a, b, c):
    
    if b == 1:
        return a % c
    if b%2==0:
        return power(a**2 %c, b//2, c) % c
    return (a * power(a**2 %c, (b-1)//2, c)) % c

a,b,c=map(int,input().split())
print(power(a, b, c))