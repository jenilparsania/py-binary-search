"""
Problem statement
You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.



Implement the ‘upperBound’ function to find the index of the upper bound of 'x' in the array.



Note:
The upper bound in a sorted array is the index of the first value that is greater than a given value. 
If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
We are using 0-based indexing.
Try to write a solution that runs in log(n) time complexity.


Example:

Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,

Output: 2

Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).
Sample Input 1:
5 7
1 4 7 8 10


Sample Output 1:
3   


Explanation of sample output 1:
In the given test case, the lowest value greater than 7 is 8 and is present at index 3(0-indexed). 
"""



def upperBound(arr: list, x: int, n: int) -> int:
    # Write your code here.
    low = 0
    high = n-1
    ub = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<x:
            low = mid + 1
        else:
            ub = mid
            high = mid-1

    return ub