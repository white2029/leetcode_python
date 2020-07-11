#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
#
# algorithms
# Hard (53.37%)
# Likes:    222
# Dislikes: 4
# Total Accepted:    6.8K
# Total Submissions: 12.7K
# Testcase Example:  '[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]'
#
# Given a m x n grid. Each cell of the grid has a sign pointing to the next
# cell you should visit if you are currently in this cell. The sign of
# grid[i][j] can be:
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to
# grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to
# grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
# 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
# 1][j])
#
#
# Notice that there could be some invalid signs on the cells of the grid which
# points outside the grid.
#
# You will initially start at the upper left cell (0,0). A valid path in the
# grid is a path which starts from the upper left cell (0,0) and ends at the
# bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
# path doesn't have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a
# cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
# change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
# (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2,
# 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
#
#
# Example 3:
#
#
# Input: grid = [[1,2],[4,3]]
# Output: 1
#
#
# Example 4:
#
#
# Input: grid = [[2,2,2],[2,2,2]]
# Output: 3
#
#
# Example 5:
#
#
# Input: grid = [[4]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
#
#
#

# @lc code=start
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m =  len(grid), len(grid[0])
        dire = [(0,1), (0,-1), (1, 0), (-1,0)]
        conn = dict()
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                ii, jj = dire[v-1]
                ni, nj = i+ii, j+jj
                if 0<=ni<n and 0<=nj<m:
                    conn[(i,j)] = ni,nj
                else:
                    conn[(i,j)] = None

        #print(conn)
        c = 0
        to_visit = {(0,0)}
        visited = set()
        while to_visit:
            iterlist = list(to_visit)
            to_visit.clear()
            for r in iterlist:
                while r and r not in to_visit:
                    to_visit.add(r)
                    r = conn[r]
            #print('updated', to_visit, c)
            visited.update(to_visit)
            if (n-1, m-1) in visited:
                return c
            next_visit = set()
            for i,j in to_visit:
                for ii, jj in dire:
                    ni, nj = i+ii, j+jj
                    if 0<=ni<n and 0<=nj<m and (ni, nj) not in visited:
                        next_visit.add((ni, nj))
            to_visit = next_visit
            c += 1





# @lc code=end
