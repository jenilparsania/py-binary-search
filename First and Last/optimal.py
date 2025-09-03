class Solution(object):
    

    def searchLeft(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        index = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                index = mid
                high = mid -1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def searchRight(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        index = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                index = mid
                low = mid +1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def searchRange(self,nums,target):
        start = self.searchLeft(nums,target)
        end = self.searchRight(nums,target)
        

        return [start,end]

        



nums = [5,7,7,8,8,10]
target = 6
print(Solution.searchRange(nums,target))