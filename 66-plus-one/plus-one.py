class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in range(len(digits)):
            res += digits[i] * 10 ** (len(digits) - i - 1) 
        return [int(i) for i in str(res+1)]