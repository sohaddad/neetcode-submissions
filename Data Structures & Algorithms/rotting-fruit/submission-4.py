class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit 
                        or grid[r + dr][c + dc] == 0
                        or grid[r+dr][c+dc] == 2):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1