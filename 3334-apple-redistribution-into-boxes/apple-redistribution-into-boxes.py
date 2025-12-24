class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity = sorted(capacity, reverse = True)
        temp = 0
        for i in range(0, len(capacity)):
            temp += capacity[i]
            if temp >= total:
                return i+1
        return temp
