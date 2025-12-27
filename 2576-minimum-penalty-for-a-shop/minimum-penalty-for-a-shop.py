class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_N = [0] * (n + 1)   # prefix_N[t] = N count for indices < t
        for i in range(n):
            prefix_N[i+1] = prefix_N[i] + (1 if customers[i] == 'N' else 0)

        suffix_Y = [0] * (n + 1)   # suffix_Y[t] = Y count for indices >= t
        for i in range(n-1, -1, -1):
            suffix_Y[i] = suffix_Y[i+1] + (1 if customers[i] == 'Y' else 0)

        best_t = 0
        best_penalty = prefix_N[0] + suffix_Y[0]  # 等于 suffix_Y[0] 实际上
        for t in range(1, n+1):
            penalty = prefix_N[t] + suffix_Y[t]
            if penalty < best_penalty:
                best_penalty = penalty
                best_t = t

        return best_t
