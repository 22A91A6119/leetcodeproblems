class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        s.sort()
        l = len(s)
        a = s[0]
        b = s[l-1]
        e = ""
        m = min(len(a),len(b))
        for i in range(m):
            if a[i] == b[i]:
                e = e + a[i]
            else:
                break
        return(e)
