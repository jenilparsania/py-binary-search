"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        ub = n
        while low<=high:
            mid = (low+high)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
                ub = mid
            else:
                low = mid +1
        return ub

nums = [1,3,5,6]
target = 2

print(searchInsert(nums,target))