def removeDuplicates(nums):
    if nums == []:
        return nums
    noDupePtr = 1
    store = nums[0]
    for item in nums:
        if (item != store):
            nums[noDupePtr] = item
            noDupePtr+=1
            store = item
    return nums

print(removeDuplicates([1,1,2])) #2
print(removeDuplicates([])) #0
print(removeDuplicates([1, 1, 1])) #1
print(removeDuplicates([1, 1,1, 4,4,4])) #2
print(removeDuplicates([1, 2,4])) #3

