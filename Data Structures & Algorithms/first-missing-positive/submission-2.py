class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        
        N = 1
        for i in range(len(hashset)):
            if N not in hashset:
                return N
            else:
                N += 1 
            
        return N

            