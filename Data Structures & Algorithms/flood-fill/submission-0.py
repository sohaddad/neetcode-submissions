class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        og_color = image[sr][sc]

        def dfs(image, r, c, visit):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or image[r][c] != og_color):
                return

            visit.add((r, c))
            image[r][c] = color

            dfs(image, r + 1, c, visit)
            dfs(image, r - 1, c, visit)
            dfs(image, r, c + 1, visit)
            dfs(image, r, c - 1, visit)
        
        dfs(image, sr, sc, set())

        return image