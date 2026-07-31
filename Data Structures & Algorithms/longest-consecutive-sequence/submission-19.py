class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hSet = (nums)
        res = 0

        for n in nums:
            if (n - 1) not in hSet:
                length = 0
                while (n + length) in hSet:
                    length += 1
                    res = max(res, length)
        return res