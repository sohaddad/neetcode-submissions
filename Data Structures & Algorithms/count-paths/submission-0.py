class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        row = [0] * COLS
        row[COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 2, -1, -1):
                row[c] = row[c] + row[c+1]

        return row[0]
