#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (42.61%)
# Likes:    1769
# Dislikes: 91
# Total Accepted:    185K
# Total Submissions: 430.3K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
#
#
#

# @lc code=start
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n19 = set(list('123456789'))
        conn = defaultdict(set)
        center = [(i,j) for i in {1,4,7} for j in {1,4,7}]
        def get_conn(i,j):
            for x in range(0, 9):
                conn[(i,j)].add((x,j))
                conn[(i,j)].add((i,x))
            for ci, cj in center:
                if abs(i-ci)<=1 and abs(j-cj)<=1:
                    for ii in range(-1,2):
                        for jj in range(-1,2):
                            ni, nj = ci + ii, cj + jj
                            conn[(i,j)].add((ni, nj))
                    break
            conn[(i,j)].discard((i,j))


        for i in range(9):
            for j in range(9):
                get_conn(i,j)

        def get_avail(i, j):
            choices = set(n19)
            for ni, nj in conn[(i,j)]:
                choices.discard(board[ni][nj])
            return choices

        to_fill = set()
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    to_fill.add((i,j))

        def solve():
            if not to_fill:
                return True
            min_avail = n19
            ci, cj = None, None
            for i, j in to_fill:
                val = get_avail(i,j)
                if not val:
                    return False
                if len(val) < len(min_avail):
                    min_avail = val
                    ci, cj = i, j
            to_fill.discard((ci, cj))
            for x in min_avail:
                board[ci][cj] = x
                if solve():
                    return True
            board[ci][cj] = '.'
            to_fill.add((ci, cj))
            return False
        print(solve())


# @lc code=end
