class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # generating array of number from [1, n]
        arr = set(range(1, len(nums) + 1))
        
        for num in nums:
            if num in arr:
                arr.remove(num)
                    
        return list(arr)