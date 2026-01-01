class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tab = defaultdict(set)
        for u, v, w in allowed:
            tab[u, v].add(w)
        
        def add_neighb(node):
            res = ['']
            for i in range(1, len(node)):
                temp = tab[(node[i-1], node[i])]
                new_res = []
                if temp:
                    for j in temp:
                        for k in res:
                            new_res.append(k + j)
                else:
                    return []
                res = new_res
            return res

        visited = set()
        def dfs(node):
            if(len(node) == 1): return True
            if node in visited: return False
            for next in add_neighb(node):
                if dfs(next):
                    return True
            visited.add(node)
            return False

        return dfs(bottom)
