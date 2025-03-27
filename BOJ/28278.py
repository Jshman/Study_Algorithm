import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == '1':
        stack.append(cmd[1])

    elif cmd[0] == '2':
        if (len(stack) == 0) :
            print(-1)
            continue
        elem = stack.pop()
        print(elem)

    elif cmd[0] == '3':
        print(len(stack))

    elif cmd[0] == '4':
        if (stack == []):
            print(1)
            continue
        print(0)
    
    else:
        if (stack == []):
            print(-1)
            continue
        print(stack[-1])