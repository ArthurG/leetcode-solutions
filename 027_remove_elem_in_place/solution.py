def removeElement(nums, val):
    lenElements = 0
    for element in nums:
        if element != val:
            nums[lenElements] = element
            lenElements += 1
    return lenElements

arr1 = [3, 2, 2, 3]
arr2 = [3, 2, 2, 3]
arr5 = []
print(removeElement(arr1, 3), arr1) #2, [2, 2...]
print(removeElement(arr2, 5), arr2) #4, [3, 2, 2, 3]
print(removeElement(arr5, 5), arr5) #0 []
