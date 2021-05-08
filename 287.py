from collections import Counter 
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = Counter(nums)
        
        # fetching all the keys
        keys = count.keys()
        # fetching maximum occurence value of a key
        max_val = max(count.values())
        
        for key in keys:
            if max_val == count[key]:
                return key