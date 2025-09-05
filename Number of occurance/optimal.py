class Solution:
    
    def countLeft(self,arr,n,x):
        low = 0
        high = n-1
        index = 0
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==x:
                index = mid 
                high = mid -1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return index

    def countRight(self,arr,n,x):
        low = 0
        high = n-1
        index = -1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==x:
                index = mid 
                low = mid +1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return index
        
    def count(self,arr, n, x):
		# code here
        # n:size x:target
        start = self.countLeft(arr,n,x)
        end = self.countRight(arr,n,x)
        
        return end-start+1




target = 2
arr = [1, 1, 2, 2, 2, 2, 3]
n = len(arr)