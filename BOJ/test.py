import random
nums = []
for i in range(32):
    nums.append(random.randint(1, 100))
nums = list(set(nums))
nums.sort()
print(nums)