class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0

            maxOne = max(maxOne, count)
        return maxOne