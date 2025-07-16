class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = list()
        for item in s:
            if ans and item == ans[-1]: ans.pop()
            else: ans.append(item)
        return ''.join(ans)
        