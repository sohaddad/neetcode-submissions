class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        row = [0] * COLS

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    row[c] = 0
                elif r == ROWS - 1 and c == COLS - 1:
                    row[c] = 1
                else:
                    right = row[c + 1] if c + 1 < COLS else 0
                    row[c] = row[c] + right

        return row[0]