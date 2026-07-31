class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res = []

        l, r = 0, k - 1
        max_n = 0

        for r in range(k, N + 1):
            highest_num = max(nums[l:r], default=0)
            res.append(highest_num)
            l += 1

        return res

