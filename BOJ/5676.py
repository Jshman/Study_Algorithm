# 5676 음주 코딩

while 1:
    try:
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        ans = ""
        tree = [0] * (N*4)

        def init(start, end, idx):
            if start == end:
                tree[idx] = 1 if arr[end] > 0 else (0 if arr[end] == 0 else -1)
                return tree[idx]
            mid = (start+end)//2
            tmp = init(start, mid, idx*2) * init(mid+1, end, idx*2+1)
            tree[idx] = 1 if tmp > 0 else (0 if tmp == 0 else -1)
            return tree[idx]

        def update(start, end, idx, where, differ):
            if where < start or end < where:
                return
            tree[idx] += differ
            if start == end:
                return
            mid = (start+end)//2
            update(start, mid, idx*2, where, differ)
            update(mid+1, end, idx*2+1, where, differ)

        def interval(start, end, idx, left, right):
            if end < left or right < start:
                return 1
            
            if left <= start and end <= right:
                return tree[idx]
            
            mid = (start+end)//2
            
            return interval(start, mid, idx*2, left, right) * interval(mid+1, end, idx*2+1, left, right)

        init(0, N-1, 1)

        for __ in range(K):
            cmd, a, b = input().split()
            if cmd == "C":
                update(0, N-1, 1, int(a)-1, int(b) - arr[int(a)-1])
            else:
                result = interval(0, N-1, 1, int(a)-1, int(b)-1)
                if result > 0 : ans += "+"
                elif result == 0 : ans += "0"
                else: ans += "-"
        print(ans)
    except:
        break



