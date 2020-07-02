#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#
# https://leetcode.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (53.84%)
# Likes:    1140
# Dislikes: 18
# Total Accepted:    120.6K
# Total Submissions: 223.2K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# You are given a m x n 2D grid initialized with these three possible
# values.
#
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than
# 2147483647.
#
#
# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.
#
# Example: 
#
# Given the 2D grid:
#
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
# ⁠ 0  -1 INF INF
#
#
# After running your function, the 2D grid should be:
#
#
# ⁠ 3  -1   0   1
# ⁠ 2   2   1  -1
# ⁠ 1  -1   2  -1
# ⁠ 0  -1   3   4
#
#
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        to_visit = set()
        empty = set()
        obstc = set()

        for i, row in enumerate(rooms):
            for j, v in enumerate(row):
                if v == 0:
                    to_visit.add((i,j))
                elif v == -1:
                    obstc.add((i,j))
                else:
                    empty.add((i,j))
        dire = [[-1,0],[1,0],[0,1],[0,-1]]
        depth = 0
        while to_visit:
            next_visit = set()
            for i, j in to_visit:
                rooms[i][j] = depth
            for i, j in to_visit:
                for ii, jj in dire:
                    ni, nj = ii + i, jj + j
                    if (ni, nj) in empty:
                        next_visit.add((ni, nj))
                        empty.discard((ni, nj))
            to_visit = next_visit
            depth += 1





# @lc code=end
