from collections import Counter 
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = Counter(nums)
        
        keys = count.keys()
        max_val = max(count.values())
        
        for key in keys:
            if max_val == count[key]:
                return key