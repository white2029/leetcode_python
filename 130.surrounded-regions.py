#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (26.58%)
# Likes:    1747
# Dislikes: 653
# Total Accepted:    236.2K
# Total Submissions: 854.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        maps = dict()
        sets = dict()
        def build(x):
            nonlocal maps
            nonlocal sets

            if x not in maps:
                xs = {x}
                maps[x] = xs
                sets[id(xs)] = xs

        def union(x, y):
            nonlocal maps
            nonlocal sets

            xs, ys = maps[x], maps[y]
            if xs is ys:
                return
            if len(xs) < len(ys):
                xs, ys = ys, xs
            xs.update(ys)
            for i in ys:
                maps[i] = xs
            sets.pop(id(ys), None)

        dire = [(-1,0),(1,0),(0,-1),(0,1)]
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 'O':
                    build((i,j))
                    for ii, jj in dire:
                        ni, nj = ii+i, jj+j
                        if (ni,nj) in maps:
                            union((i,j), (ni,nj))
        n = len(board)
        m = len(board[0])
        #print(sets.values())
        for group in sets.values():
            edge = False
            for i,j in group:
                if i==0 or j==0 or i==n-1 or j==m-1:
                    edge = True
                    break
            if not edge:
                for i, j in group:
                    board[i][j] = 'X'



# @lc code=end
