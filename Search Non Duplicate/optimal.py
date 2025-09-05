"""
TC -> O(log N )
SC -> O(1)
"""

def singleNonDuplicate(arr):
    # Write your code here
    n = len(arr)
    low = 0
    high = n-1
    # would have to cover the edge cases

    if n==1:
        return arr[0]
    
    if  arr[0] != arr[1] :
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    while low<=high:
        mid = (low+high)//2
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]

        if arr[mid] == arr[mid-1]:
            if mid % 2==0:
                 # it is even
                 high = mid -1
            else:
                low = mid +1
        elif arr[mid]==arr[mid+1]:
            if mid %2==0:
                low = mid +1
            else:
                high = mid - 1
                

arr=[1,1,2,2,5,7,7,8,8,9,9]
print(singleNonDuplicate(arr))