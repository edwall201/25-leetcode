class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0 
        negative_count = 0
        min_abs_sum = float('inf')
        for row in matrix:
            for value in row:
                res += abs(value)
                if value < 0:
                    negative_count +=1
                min_abs_sum = min(min_abs_sum, abs(value))
        if negative_count % 2 == 1:
            res -= 2 * min_abs_sum
        
        return res
        