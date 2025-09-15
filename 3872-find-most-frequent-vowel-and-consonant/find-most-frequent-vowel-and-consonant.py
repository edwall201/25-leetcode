class Solution:
    def maxFreqSum(self, s: str) -> int:
        con, vow = 0, 0
        for i in set(s):
            if i in "aeiou":
                con = max(con, s.count(i))
            else: vow = max(vow, s.count(i))
        return con + vow