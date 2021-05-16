class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        arr = [1, 1]
        
        for i in range(2, n+1):
            
            # getting the sum of previous two elements in the array: fibonnaci series
            arr.append(arr[i-1] + arr[i-2]) 
        
        return arr[n] 
        