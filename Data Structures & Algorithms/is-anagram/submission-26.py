class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)

        return counterS == counterT