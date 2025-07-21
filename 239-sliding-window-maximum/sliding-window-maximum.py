class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        keep_num = deque()
        for i in range(len(nums)):
            update_num(keep_num, nums[i])
            if i >= k and keep_num[0] == nums[i - k]:
                keep_num.popleft()
            if i >= k - 1:
                res.append(keep_num[0])
        return res
def update_num(keep_num, num):
        while keep_num and num > keep_num[-1]:
            keep_num.pop()
        keep_num.append(num)

             
        