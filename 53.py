from sys import maxsize

# returning the sum of the maximum Sub Array.
def maxSubArraySum(nums):

    max_sum = nums[0]
    cur_sum = 0

    for n in nums:

    	# we make the current sum equal to 0, if it becomes negative.
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        # since we need to return the sum
        # and not the subarray, so keeping
        # the max does the job
        max_sum = max(max_sum, cur_sum)

    return max_sum

# in case if you want to return an array as well

def maxSubArray(nums):
    max_so_far = -maxsize - 1  # dealing with all negative array
    iterator = nums[0]
    start, end = 0, 0
    cur_sum = 0

    for i in range(len(nums)):

    	# assigning values from the iterator
        if max_so_far < iterator:
            max_so_far = iterator
            start = cur_sum
            end = i

        # if iterator becomes negative, we make it zero and move cur_sum pointer forward
        if iterator < 0:
            iterator = 0
            cur_sum = i + 1  # moving a step forward if current sum becomes < 0

        iterator += nums[i]

    print(max_so_far) # returning largest sum
    print(nums[start-1:end]) # return the contiguous subarray with largest sum


# easy to understand brute force approach -> O(n^2) time
def brute_force(nums):

    arr = []

    # storing all the sub-arrays
    for i in range(len(nums)):
        for j in range(len(nums) + 1):

            arr.append(nums[i:j])

    max_so = -maxsize
    index = 0

    # getting the sub-array with maximum sum
    for i in range(len(arr)):

        if max_so < sum(arr[i]):
            max_so = sum(arr[i])
            index = i

    print(max_so)
    print(arr[index])

nums = [-2,1,-3,4,-1,2,1,-5,4]


#print(maxSubArraySum(nums))
#maxSubArray(nums)
