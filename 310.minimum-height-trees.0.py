#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (31.88%)
# Likes:    1794
# Dislikes: 96
# Total Accepted:    92.4K
# Total Submissions: 289.6K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
# Example 1 :
#
#
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3
#
# Output: [1]
#
#
# Example 2 :
#
#
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5
#
# Output: [3, 4]
#
# Note:
#
#
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
#
#
#

# @lc code=start
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        conn = dict()
        if not edges:
            return [0]
        for i, j in edges:
            if i not in conn:
                conn[i] = set()
            if j not in conn:
                conn[j] = set()
            conn[i].add(j)
            conn[j].add(i)
        conn2 = []
        conn1 = []
        while conn:
            if len(conn) == 2:
                conn2 = list(conn.keys())
            if len(conn) == 1:
                conn1 = list(conn.keys())
            leaves = set()
            for i, v in conn.items():
                if len(v) <= 1:
                    leaves.add(i)
            for i in leaves:
                conn.pop(i)
                for v in conn.values():
                    v.discard(i)
        return conn1 if conn1 else conn2





# @lc code=end
