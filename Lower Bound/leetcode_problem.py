"""
Problem statement
You are given an array 'arr' sorted in non-decreasing order and a number 'x'.



You must return the index of lower bound of 'x'.



Note:
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'

If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

Consider 0-based indexing.


Example:
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.
"""

def lowerBound(arr:list,n:int,target:int)->int:
    low = 0
    high = n-1
    lb = n
    while low<=high:
        mid = (high+low)//2
        if arr[mid]>=target:
            lb = mid
            high = mid-1
        else:
            low = mid +1
    
    return lb


