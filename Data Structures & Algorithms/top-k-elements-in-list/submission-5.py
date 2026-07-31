class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize dictionary 
        counts = {}
        #initialize list, sublist
        freq = [[] for i in range(len(nums) + 1)]

        #count every single element in nums array
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        #add n to the sublist base on counts
        for n, c in counts.items():
            freq[c].append(n)

        res = []
        #check the counts from descending order to see which n had the highest count and add to result array
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

