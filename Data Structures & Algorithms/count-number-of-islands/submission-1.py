class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid) #find the amount of rows
        columns = len(grid[0]) #find the amount of columns by finding amount of elements in the grid
        islands = 0 

        def dfs(r,c):
            #check out of bounds stuff
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 
            if grid[r][c] == "0":
                return 

            #check to make sure its not revisited
            grid[r][c] = "0"
            #check the directions
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands

            

        