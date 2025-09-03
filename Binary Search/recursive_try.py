#  trying the binary search in the recursive way 

def search(nums:list,target,low,high):
    mid = (low+high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid]<target:
        ans = search(nums,target,mid+1,high)
    else:
        ans = search(nums,target,low,mid-1)
    
    return ans


nums = [-1,0,3,5,9,12]
target = 9
n = len(nums)
print(search(nums,target,0,n-1))
    