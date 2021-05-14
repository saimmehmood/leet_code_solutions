class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # generating array of numbers from [1, n]
        arr = set(range(1, len(nums) + 1))
        
        for num in nums:
            if num in arr:
                arr.remove(num) # removing elements which are in both; thus getting the disappeared ones.
                    
        return list(arr)