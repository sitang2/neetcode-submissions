class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = collections.Counter(arr)

        for ch in arr:
            if count[ch] == 1:
                k -= 1
            if k == 0:
                return ch           
        return ''