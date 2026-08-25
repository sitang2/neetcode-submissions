class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [[]] * (2 * N)
        
        for i in range(N):
            res[i] = res[i + N] = nums[i]
        
        return res