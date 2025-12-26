class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        temp = 0
        happiness = sorted(happiness)
        for i in range(len(happiness)-1, -1, -1):
            happiness[i] -= temp
            if(temp == k or happiness[i] <0):
                break
            res += happiness[i]
            temp += 1
        return res

        