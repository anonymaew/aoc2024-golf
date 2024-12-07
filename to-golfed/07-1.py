
def can_solved(target,now,nums):
    if now is None:
        return can_solved(target,nums[0],nums[1:])
    if nums ==[]:
        print(now,target)
        return now==target
    return can_solved(target,now+nums[0],nums[1:]) or can_solved(target,now*nums[0],nums[1:])
    

s = 0
for l in open(0).readlines():
    target,nums = l[:-1].split(": ")
    target,nums = int(target),list(map(int,nums.split(" ")))
    if can_solved(target,None,nums):
        s+=target
print(s)
