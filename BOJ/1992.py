# 쿼드트리 (2104 풀려고 연습)

N=int(input())
inputs = [input() for _ in range(N)]

# arr는 2차원 배열
def sol(arr):
    if len(arr[0])==1:
        return arr[0][0]
    
    # 4방위가 모두 같은지 확인하는 작업
    pivot = arr[0][0]
    ret = pivot
    leng=len(arr)
    for i in range(leng):
        for j in range(leng):
            if arr[i][j] != pivot:
                tmp1 = []
                tmp2 = []
                tmp3 = []
                tmp4 = []
                for k in range(leng):
                    elem = arr[k]
                    if k < leng//2:
                        tmp1.append(elem[:leng//2])
                        tmp2.append(elem[leng//2:])
                    else:
                        tmp3.append(elem[:leng//2])
                        tmp4.append(elem[leng//2:])
                ret = "("
                for lst in [tmp1, tmp2, tmp3, tmp4]:
                    ret += sol(lst)
                ret += ")"
                return ret
    return ret

ans = sol(inputs)
print(ans)