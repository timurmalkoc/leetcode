def removeDuplicates(nums):
        i = 1
        while(len(nums) > i):
            if(nums[i-1] == nums[i]):
                del nums[i]
            else:
                i += 1
        return i

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))