#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (45.59%)
# Likes:    1855
# Dislikes: 73
# Total Accepted:    201K
# Total Submissions: 437.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
#
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
#
#
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rst = []
        def sub(row, cols, left, right, tmp):
            if row == n:
                rst.append(tmp)
            for j in cols:
                ll = row + j
                rr = row - j
                if ll in left or rr in right:
                    continue
                sub(row+1, cols-{j}, left|{ll}, right|{rr}, tmp + ['.'*j + 'Q' + '.'*(n-j-1)])
        sub(0, set(range(0,n)), set(), set(), [])
        return rst
# @lc code=end
