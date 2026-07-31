class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, list in enumerate(matrix):
            if target <= list[-1]:
                l, r = 0, len(list) - 1
                while l <= r:
                    m = l + ((r - l) // 2)
                    if list[m] > target:
                        r = m - 1
                    elif list[m] < target:
                        l = m + 1
                    else:
                        return True
                return False
            
        return False