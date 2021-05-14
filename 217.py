class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new_arr = list(set(nums))
        
        new_arr.sort()
        nums.sort()
        
        if new_arr == nums:
            return False
        
        return True