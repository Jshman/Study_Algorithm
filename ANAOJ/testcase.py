import random

def random_name_generator():
    name_length = random.randint(1, 19)
    s = ""
    for i in range(name_length):
        s += str(chr(random.randint(65, 90)))
    return s

def random_age_generator():
    return random.randint(0, 131)

if __name__ == "__main__":
    n = 10
    # results = []
    # for _ in range(n):
    #     results.append((random_name_generator(), random_age_generator()))
    #
    # for info in results:
    #     print(*info)
    for i in range(n):
        print(random_age_generator())