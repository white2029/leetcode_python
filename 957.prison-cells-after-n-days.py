#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#
# https://leetcode.com/problems/prison-cells-after-n-days/description/
#
# algorithms
# Medium (39.62%)
# Likes:    667
# Dislikes: 940
# Total Accepted:    86.1K
# Total Submissions: 207.9K
# Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'
#
# There are 8 prison cells in a row, and each cell is either occupied or
# vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
#
#
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
#
#
# (Note that because the prison is a row, the first and the last cells in the
# row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way: cells[i] ==
# 1 if the i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N
# days (and N such changes described above.)
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
#
#
#
# Example 2:
#
#
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
#
#
#
#
# Note:
#
#
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9
#
#
#
#
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = OrderedDict()

        def get_next(pos):
            rst = [0]
            for i in range(1, len(pos)-1):
                if pos[i-1] == pos[i+1]:
                    rst.append(1)
                else:
                    rst.append(0)
            rst.append(0)
            #print('from', pos, 'to', rst)
            return tuple(rst)

        n = 1
        pos = tuple(cells)
        visited[pos] = len(visited)
        while n <= N:
            n += 1
            pos = get_next(pos)
            if pos in visited:
                break
            visited[pos] = len(visited)

        #print('pos', pos, n)
        if n == N+1:
            return pos

        recur_start = visited[pos]
        recur_len = len(visited) - recur_start
        start_len = len(visited) - recur_len
        rem = (N+1-start_len) % recur_len
        pos_idx = recur_start + (rem - 1) % recur_len
        #print('recur_start', recur_start, 'recur_len', recur_len, 'start_len', start_len, 'rem', rem, pos_idx)

        val = None
        for k, v in visited.items():
            #print(k, v)
            if v == pos_idx:
                val = list(k)

        return val
# @lc code=end
