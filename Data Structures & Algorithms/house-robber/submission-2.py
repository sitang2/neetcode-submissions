class Solution:
    def rob(self, nums: List[int]) -> int:
        #Array nums = list of houses 
        #nums[i] = each house have certain amount of money

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2