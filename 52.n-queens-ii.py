#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (57.04%)
# Likes:    505
# Dislikes: 150
# Total Accepted:    132.9K
# Total Submissions: 231.8K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
#
# Example:
#
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
#
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
#
#
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        rst = 0
        def sub(row, cols, left, right):
            nonlocal rst
            if row == n:
                rst += 1
            for j in cols:
                ll = row + j
                rr = row - j
                if ll in left or rr in right:
                    continue
                sub(row+1, cols-{j}, left|{ll}, right|{rr})
        sub(0, set(range(0,n)), set(), set())
        return rst
#

# @lc code=end
