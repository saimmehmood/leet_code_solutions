class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # getting a list of distinct elements
        new_arr = list(set(nums))
        
        # sorting and comparing the lists/arrays
        new_arr.sort()
        nums.sort()
        
        if new_arr == nums:
            return False
        
        return True