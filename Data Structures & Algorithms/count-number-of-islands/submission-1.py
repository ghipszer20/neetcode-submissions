class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def exploreIsland(grid: List[List[str]], i: int, j: int) -> None:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != "1":
                return
            
            grid[i][j] = "Visited"

            exploreIsland(grid, i + 1, j)
            exploreIsland(grid, i - 1, j)
            exploreIsland(grid, i, j + 1)
            exploreIsland(grid, i, j - 1)

        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    exploreIsland(grid, i, j)
                    

        return islands
        


        