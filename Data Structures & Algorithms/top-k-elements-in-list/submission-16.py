class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]
        
        # count n
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # add n in freq array based on count
        for n, c in count.items():
            freq[c].append(n)
        
        #add it to the result based on highest count
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res