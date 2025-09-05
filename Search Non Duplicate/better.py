def searchNonDuplicate(nums:list):
    n= len(nums)
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    for i in range(1,n-1):
        if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
            return nums[i]


nums = [1,1,1,2,2,3,4,4,4,5,5]
print(searchNonDuplicate(nums)) 
    