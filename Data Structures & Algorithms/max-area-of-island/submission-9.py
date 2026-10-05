class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        largest = 0
        visit = set()

        def dfs(grid, r, c, visit):
            nonlocal temp
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 0):
                return 

            visit.add((r, c))
            temp += 1
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    temp = 0
                    dfs(grid, r, c, visit)
                    if temp >= largest:
                        largest = temp

        return largest