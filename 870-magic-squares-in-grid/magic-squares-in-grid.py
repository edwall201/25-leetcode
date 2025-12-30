class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row < 3 or col <3: return 0

        def is_magic(row, col):
            val = []
            for i in range(row, row + 3):
                for j in range(col, col +3):
                    v = grid[i][j]
                    if v < 1 or v > 9: return False
                    val.append(v)
            if(3 not in val): return False
            if(len(val) != 9): return False
            if (grid[row + 1][col + 1] != 5): return False
            
            for i in range(row, row +3):
                if sum(grid[i][col:col+3]) != 15: return False

            for i in range(col, col +3):
                if grid[row][i] + grid[row +1][i] + grid[row + 2][i] != 15: return False
            
            if grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col+2] != 15: return False
            if grid[row][col + 2 ] + grid[row + 1][col + 1] + grid[row + 2][col] != 15: return False

            return True
        res = 0
        for i in range(row - 2):
            for j in range(col - 2):
                if is_magic(i, j): res += 1
        return res
                
        