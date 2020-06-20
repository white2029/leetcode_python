#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (51.00%)
# Likes:    3074
# Dislikes: 113
# Total Accepted:    275.7K
# Total Submissions: 540.2K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0

        @lru_cache(maxsize=None)
        def cnt(vals):
            if vals <= 1:
                return 1
            else:
                ttl = 0
                for i in range(0, vals):
                    left = i
                    right = vals -i -1
                    lsub = cnt(left)
                    rsub = cnt(right)
                    ttl += lsub * rsub
            return ttl
        return cnt(n)


# @lc code=end
