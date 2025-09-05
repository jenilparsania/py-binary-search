"""
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.

"""

def count(arr, n, x):
		# code here
        # n:size x:target
        low = 0
        high = n-1
        count = 0
        while low<=high:
            mid = (low+high)//2
            if arr[mid] >x:
                high = mid - 1
            elif arr[mid]<x:
                low = mid + 1 
            
            if arr[mid]==x:
                count += 1
        
        return count


target = 2
arr = [1, 1, 2, 2, 2, 2, 3]
n = len(arr)

print(count(arr,n,target))


