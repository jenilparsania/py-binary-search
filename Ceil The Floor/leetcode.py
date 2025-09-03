"""
Problem statement
You're given a sorted array 'a' of 'n' integers and an integer 'x'.



Find the floor and ceiling of 'x' in 'a[0..n-1]'.



Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.


Example:
Input: 
n=6, x=5, a=[3, 4, 7, 8, 8, 10]   

Output:
4

Explanation:
The floor and ceiling of 'x' = 5 are 4 and 7, respectively.

Sample Input 1 :
6 8
3 4 4 7 8 10


Sample Output 1 :
8 8


Explanation of sample input 1 :
Since x = 8 is present in the array, it will be both floor and ceiling.


Sample Input 2 :
6 2
3 4 4 7 8 10
"""

def getFloorAndCeil(a, n, x):
    # Write your code here.
    #  a : array ; n:len(a) ; x:target
    low = 0
    high = n-1
    floor = -1
    ceil = -1
    while low<=high:
        mid = (low+high)//2
        if a[mid] <=x:
            low = mid + 1
            floor = a[mid]
        else:
            high = mid - 1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if a[mid]>=x:
            ceil = a[mid]
            high = mid -1
        else:
            low = mid + 1
    
    return [floor,ceil]





nums = [2,3,7,7,8,11,16,17,27,28]
target = 19
n = len(nums)

print(getFloorAndCeil(nums,n,target))