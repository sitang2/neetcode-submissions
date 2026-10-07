class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        twoD = N * N
        counts = [0] * twoD
                
        for nums in grid:
            for num in nums:
                counts[num - 1] += 1

        res = [0] * 2

        print(counts)
        for i, c in enumerate(counts):
            if c == 2:
                res[0] = i + 1
            
            if c == 0:
                res[1] = i + 1

        return res