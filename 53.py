from sys import maxsize

# returning the sum of the maximum Sub Array.
def maxSubArraySum(nums):

    max_sub = nums[0]
    cur_sub = 0

    for n in nums:

        if cur_sub < 0:
            cur_sub = 0
        cur_sub += n
        # since we need to return the sum
        # and not the subarray, so keeping
        # the max does the job
        max_sub = max(max_sub, cur_sub)

    return max_sub

# in case if you want to return an array as well

def maxSubArray(nums):
    max_so_far = -maxsize - 1  # dealing with negative array
    max_end = nums[0]
    start, end = 0, 0
    cur_sub = 0

    for i in range(len(nums)):

        if max_so_far < max_end:
            max_so_far = max_end
            start = cur_sub
            end = i

        if max_end < 0:
            max_end = 0
            cur_sub = i + 1  # moving a step forward if current sum becomes < 0

        max_end += nums[i]

    print(max_so_far)
    print(nums[start-1:end])

# easy to understand brute force approach
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
