class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        #count
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #add to freq based on count
        for i, c in count.items():
            freq[c].append(i)

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 