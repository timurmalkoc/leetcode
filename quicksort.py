import random
def sortArray(nums):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return sortArray(lt) + eq + sortArray(gt)

print(sortArray([5,2,3,1]))
print(sortArray([5,1,1,2,0,0]))