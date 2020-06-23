#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (41.79%)
# Likes:    981
# Dislikes: 35
# Total Accepted:    126.4K
# Total Submissions: 302.2K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
#
# Example 1:
#
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
#
#

# @lc code=start

from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if n == 1:
            return True

        con = defaultdict(set)
        for i,j in edges:
            con[i].add(j)
            con[j].add(i)
        for i in range(0,n):
            if i not in con:
                return False
        to_visit = {0}
        visited = set()
        while to_visit:
            visited.update(to_visit)
            next_visit = set()
            for i in to_visit:
                while con[i]:
                    j = con[i].pop()
                    con[j].remove(i)
                    if j in visited:
                        return False
                    next_visit.add(j)
            to_visit = next_visit
        return len(visited) == n
# @lc code=end
