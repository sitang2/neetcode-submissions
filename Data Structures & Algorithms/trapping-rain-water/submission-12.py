class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height) - 1

        l, r = 0, N
        maxL = height[l]
        maxR = height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                if maxL - height[l] > 0:
                    res += (maxL - height[l])
                else:
                    maxL = max(maxL, height[l])
            else:
                r -= 1
                if maxR - height[r] > 0:
                    res += (maxR - height[r])
                else:
                    maxR = max(maxR, height[r])

        return res