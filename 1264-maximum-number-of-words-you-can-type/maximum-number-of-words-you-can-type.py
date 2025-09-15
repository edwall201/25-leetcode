class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0
        for t in text.split():
            if not (set(t) & broken):count += 1
        return count
        