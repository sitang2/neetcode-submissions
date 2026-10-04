class Solution:
    def maxDifference(self, s: str) -> int:

        countS = collections.Counter(s)
        res = float('-inf')

        for odd in countS.values():
            if odd % 2 == 0: 
                continue
            for even in countS.values():
                if even % 2 == 1: 
                    continue
                res = max(res, odd - even)
        return res