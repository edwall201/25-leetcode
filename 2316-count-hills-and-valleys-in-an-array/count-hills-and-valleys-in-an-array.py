class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: temp.append(nums[i])
        for i in range(1, len(temp) - 1):
            if temp[i - 1] < temp[i] > temp[i +1]: res+=1
            elif temp[i - 1] > temp[i] < temp[i +1]: res+=1
        return res