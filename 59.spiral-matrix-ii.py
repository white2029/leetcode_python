#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (52.96%)
# Likes:    948
# Dislikes: 110
# Total Accepted:    191.6K
# Total Submissions: 359.8K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dire = [(0,1), (1,0), (0,-1), (-1,0)]
        rst = [[0] * n for __ in range(n)]
        i = j = v = d = 0
        while True:
            v += 1
            if not(0<=i<n) or not(0<=j<n) or rst[i][j] != 0:
                break
            rst[i][j] = v
            di, dj = dire[d]
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<n and rst[ni][nj] == 0:
                pass
            else:
                d = (d+1)%4
                di, dj = dire[d]
                ni, nj = i + di, j + dj
            i, j = ni, nj
        return rst


# @lc code=end
