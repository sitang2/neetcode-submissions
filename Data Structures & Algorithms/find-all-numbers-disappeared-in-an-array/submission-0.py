class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [ 0 for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            count[n] += 1

        for i in range(1, len(count)):
            if count[i] == 0:
                res.append(i)

        return res

        
