def before(n):
    return 175 * (1-0.995**n)

def after(n):
    return 200 * (1-0.997**n)

for i in range(0, 1001, 100):
    print(f"{i} :\tbefore:{before(i)}\n\tafter: {after(i)}\n")

i = 835
print(f"{i} :\tbefore:{before(i)}\n\tafter: {after(i)}\n")