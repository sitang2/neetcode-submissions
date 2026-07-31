class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        maxSum = nums[0]
        curSum = 0 

        if N <= 1:
            return maxSum

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum