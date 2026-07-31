class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, count in count.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res