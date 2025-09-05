"""
Problem statement
You are given an array 'arr' having 'n' distinct integers sorted in ascending order. The array is right rotated 'r' times



Find the minimum value of 'r'.



Right rotating an array means shifting the element at 'ith' index to (‘i+1') mod 'n' index, for all 'i' from 0 to ‘n-1'.



Example:
Input: 'n' = 5 , ‘arr’ = [3, 4, 5, 1, 2]

Output: 3 

Explanation:
If we rotate the array [1 ,2, 3, 4, 5] right '3' times then we will get the 'arr'. Thus 'r' = 3.
"""

#  if we look at the loophole then the index of the minimum element would be the minimum number
#  of rotations 

def findKRotation(arr : list) -> int:
    # Write your code here.
    low = 0
    n = len(arr)
    high = n-1
    inex = 0
    minimum = float("inf")
    if arr[low]<=arr[high]:
        return 0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=arr[high]:
            # minimum = min(minimum,arr[mid])
            if arr[mid]<minimum:
                minimum = arr[mid]
                index = mid 
            high = mid - 1

        else:
            # minimum = min(minimum,arr[low])
            if arr[low]<minimum:
                minimum = arr[low]
                index = low
            low = mid + 1
        
    return index