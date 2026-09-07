class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIsland(grid: List[List[str]], i: int, j: int, seen: set(tuple)) -> None:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0" or (i, j) in seen:
                return
            
            seen.add((i, j))

            exploreIsland(grid, i + 1, j, seen)
            exploreIsland(grid, i - 1, j, seen)
            exploreIsland(grid, i, j + 1, seen)
            exploreIsland(grid, i, j - 1, seen)

        islands = 0
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    islands += 1
                    exploreIsland(grid, i, j, seen)
                    

        return islands
        


        