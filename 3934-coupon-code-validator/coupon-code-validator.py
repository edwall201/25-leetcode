class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        count = len(code)
        business = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        for i in range(count):
            temp = True
            if code[i] == "":
                continue
            for ch in code[i]:
                c = ord(ch)
                if not(48 <= c <= 57 or 65 <= c <= 90 or 97 <= c <= 122 or c == 95):
                    temp = False
            if(temp and isActive[i] and businessLine[i] in business):
                res.append((business[businessLine[i]], code[i]))
        res.sort(key = lambda x:(x[0], x[1]))
        return [j for i, j in res]
        
        