class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: 
            #check if the number is already in hashset
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False