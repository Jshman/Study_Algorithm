# 1747

# 팰린드롬 판정
def palindrome(String):
    for s in range(len(String)//2):
        if String[s] != String[-1-s]:
            return False
    return True

# 소수판정
k = 10**7 + 1
nums = [True] * k #True:소수
prime_palindrome = []

for i in range(2, k):
    if nums[i]:
        if palindrome(str(i)):
            prime_palindrome += [i]
        for j in range(i+i, k, i):
            nums[j] = False

N = int(input())
for prime in prime_palindrome:
    if prime >= N:
        print(prime)
        break