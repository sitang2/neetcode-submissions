class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashSet = set(nums)

        for num in hashSet:
            if (num - 1) not in hashSet:
                length = 0
                while (num + length) in hashSet:
                    length += 1
                res = max(res, length)
            
        return res