class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()[-1]
        b=len(a)
        return b
        