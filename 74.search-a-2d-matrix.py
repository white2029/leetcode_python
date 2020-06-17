#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (36.30%)
# Likes:    1678
# Dislikes: 154
# Total Accepted:    317.8K
# Total Submissions: 875.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [row[0] for row in matrix if row]
        l, h = 0, len(rows)-1
        if not matrix:
            return False
        if not rows:
            return False

        while l<h:
            m = l + (h-l)//2
            v = rows[m]
            if v == target:
                return True
            if l == m:
                if rows[h] > target:
                    h = l
                else:
                    l = h
                break
            if v > target:
                h = m - 1
            else:
                l = m

        print(l, h)
        if not (matrix[l][0] <= target <= matrix[l][-1]):
            return False

        rows = matrix[l]
        l, h = 0, len(rows)-1

        while l<=h:
            m = l + (h-l)//2
            v = rows[m]
            if v == target:
                return True
            if v > target:
                h = m - 1
            else:
                l = m + 1

        return False
# @lc code=end
