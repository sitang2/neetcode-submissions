class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        res = [0] * N
        rightMax = -1
        for i in range(N - 1, -1, -1):
            res[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return res
