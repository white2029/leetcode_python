#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (55.45%)
# Likes:    729
# Dislikes: 18
# Total Accepted:    96.7K
# Total Submissions: 174K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
#
# Example 1:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
#
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
#
# Output:  1
#
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        maps = {x:{x} for x in range(0,n)}
        cnt = n

        def union(x,y):
            nonlocal maps
            nonlocal cnt
            if maps[x] is maps[y]:
                return
            xs, ys = maps[x], maps[y]
            if len(xs) < len(ys):
                xs, ys = ys, xs
            xs.update(ys)
            for i in ys:
                maps[i] = xs
            cnt -= 1

        for x, y in edges:
            union(x,y)
        return cnt

# @lc code=end
