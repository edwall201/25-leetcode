class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        colunm = len(strs[0])
        delete_count = 0
        for c in range(colunm):
            for r in range(row -1):
                if strs[r][c] > strs[r+1][c]:
                    delete_count +=1 
                    break
        return delete_count