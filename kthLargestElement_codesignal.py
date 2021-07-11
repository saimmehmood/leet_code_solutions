def kthLargestElement(nums, k):
    
    # sorting and reversing bring kth largest element at the begining
    nums.sort()
    nums.reverse()
    
    return nums[k-1]
