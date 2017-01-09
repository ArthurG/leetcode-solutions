def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a =  {}
    for number in nums:
        if number not in a:
            a[number] = 1
        else:
            a[number]+=1
    for key in a:
        if a[key] == 1:
            return key
