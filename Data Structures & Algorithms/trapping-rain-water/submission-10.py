class Solution:
    def trap(self, height: List[int]) -> int:
        #Non negative int
        #Array height
        #height[i] = height of bar with width of 1
        H = len(height)
        l, r = 0, H - 1
        res = 0
        maxL = height[l] 
        maxR = height[r]
        
        while l < r:
            #if 0 <= 1
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


            
            