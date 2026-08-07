class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        N = len(heights)

        l, r = 0, N - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = minHeight * (r - l)
            maxArea = max(maxArea, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea