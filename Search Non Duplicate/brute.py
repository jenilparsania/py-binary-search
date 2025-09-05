"""
Problem statement
You are given a sorted array ‘arr’ of ‘n’ numbers such that every number occurred twice in the array except one, which appears only once.



Return the number that appears once.



Example:
Input: 'arr' = [1,1,2,2,4,5,5]

Output: 4 

Explanation: 
Number 4 only appears once the array.


Note :
Exactly one number in the array 'arr' appears once.
"""

def singleNonDuplicate(arr):
    # Write your code here
    count = 0
    n = len(arr)
    #  can do it with using the hash_map
    hash_map = dict()
    for num in arr:
        hash_map[num] = hash_map.get(num,0)+1

    for key , values in hash_map.items():
        if values==1:
            return key


nums = [1,1,1,2,3,3]
print(singleNonDuplicate(nums))  