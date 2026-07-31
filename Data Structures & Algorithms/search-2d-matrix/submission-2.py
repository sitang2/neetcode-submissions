from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, list in enumerate(matrix):
            # If the target could be in this row
            if target <= list[-1]:
                l, r = 0, len(list) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if list[m] < target:
                        l = m + 1
                    elif list[m] > target:
                        r = m - 1
                    else:
                        return True
                # If we finish the binary search and not found
                return False
        return False
