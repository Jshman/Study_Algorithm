x,y,z = map(int, input().split())
u,v,w = map(int, input().split())

ans = u//100 * x + v//50 * y + w//20 * z
print(ans)