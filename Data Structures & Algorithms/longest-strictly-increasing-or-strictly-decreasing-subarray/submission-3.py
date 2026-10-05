class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                inc = dec = 1
            elif nums[i] > nums[i - 1]:
                inc = inc + 1
                dec = 1
            else:
                dec = dec + 1
                inc = 1
            
            longest = max(longest, inc, dec)
        return longest
            
