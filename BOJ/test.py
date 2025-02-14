String = "123456543211"

def palindrome(String):
    for s in range(len(String)//2):
        print(s)
        if String[s] != String[-1-s]:
            return False
    return True

print(palindrome(String))