class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set()

        for num in nums:
            if num in collection:
                return True
            collection.add(num)
        return False