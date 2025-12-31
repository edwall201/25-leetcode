class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        return (n - 1) if (total % 2 == 0) else 0
        

        