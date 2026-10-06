class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = nums[n]
        maxAdd = 0

        for i in range(n - 1, -1, -1):
            print(i)
            if nums[i] < nums[i + 1]:
                res += nums[i]
            else:
                res = nums[i]
            
            maxAdd = max(maxAdd, res)
            print(maxAdd)
        return maxAdd