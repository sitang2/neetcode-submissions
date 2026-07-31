class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()

        for n in nums:
            if n > 0:
                hashset.add(n)
        
        N = 1
        for i in range(len(hashset)):
            if N not in hashset:
                return N
            else:
                N += 1 
            
        return N

            