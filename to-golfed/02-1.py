import sys

def check_safe(nums):
    diff = nums[1] - nums[0]
    if diff == 0:
        return 0
    direction = 1 if diff > 0 else -1
    for i, num in enumerate(nums):
        if i == 0:
            continue
        diff = num - nums[i-1]
        if not (1 <= direction*diff <= 3):
            return 0
    return 1


# def check_quite_safe(nums):
#     if check_safe(nums):
#         return True
#     for i in range(len(nums)):
#         new_nums = (nums+[])
#         new_nums.pop(i)
#         if check_safe(new_nums):
#             return True
#     return False


count_safe = 0
part=1
for line in sys.stdin:
  nums = [int(s) for s in line.split()]
  count_safe += 1 if check_safe(nums) else 0

print(count_safe)
