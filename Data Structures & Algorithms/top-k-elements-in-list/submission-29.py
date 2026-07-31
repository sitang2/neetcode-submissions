from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for n in range(len(nums) + 1)]
        countNums = Counter(nums)
        res = []

        for i, n in countNums.items():
            freq[n].append(i)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        