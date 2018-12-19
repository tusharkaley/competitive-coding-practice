class Solution:

    def identify_cell_type(self, index, ):
        return 0

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                perimeter = perimeter + identify_cell_type()