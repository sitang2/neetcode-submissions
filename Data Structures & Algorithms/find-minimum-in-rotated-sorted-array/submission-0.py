class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Given:
            #array sorted array n 0 > n
            #rotated right atlest 1 or n time

        #num unique
        #time complexity aim for O(log n)
        return min(nums)