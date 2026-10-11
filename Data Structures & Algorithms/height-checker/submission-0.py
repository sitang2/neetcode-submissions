class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedlist = sorted(heights)

        count = 0
        for i in range(len(heights)):
            if heights[i] != sortedlist[i]:
                count += 1
        
        return count