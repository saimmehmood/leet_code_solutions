from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = Counter(nums) # generating a dictionary
        arr = list(count.keys()) # getting keys

        for i in range(len(arr)):
            if count[int(arr[i])] == 1: # getting the value with single existence
                return int(arr[i])
        