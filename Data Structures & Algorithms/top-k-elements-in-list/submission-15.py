class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        #count n
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #add n in the freq sublist
        for n, c in count.items():
            freq[c].append(n)

        #return the list of array based on highest counts
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res