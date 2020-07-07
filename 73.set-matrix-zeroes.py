#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (42.75%)
# Likes:    2081
# Dislikes: 299
# Total Accepted:    315.2K
# Total Submissions: 734.6K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
#
#
# Input:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == 0:
                    for ii in range(0, m):
                        if matrix[ii][j] != 0:
                            matrix[ii][j] = '.'
                    for jj in range(0, n):
                        if matrix[i][jj] != 0:
                            matrix[i][jj] = '.'

        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == '.':
                    matrix[i][j] = 0
        return

# @lc code=end
