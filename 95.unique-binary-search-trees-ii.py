#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (39.85%)
# Likes:    2075
# Dislikes: 158
# Total Accepted:    187.7K
# Total Submissions: 470.6K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Constraints:
#
#
# 0 <= n <= 8
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def sub(vals):
            if len(vals) == 0:
                return [None]
            if len(vals) == 1:
                return [TreeNode(vals[0])]
            rst = []
            for i in range(0, len(vals)):
                left = vals[0:i]
                right = vals[i+1:len(vals)]
                lsub = sub(left)
                #print('left', left, lsub)
                rsub = sub(right)
                #print('right', right, rsub)
                for l in lsub:
                    for r in rsub:
                        o = TreeNode(vals[i])
                        o.left = l
                        o.right = r
                        rst.append(o)
            #print(vals, rst)
            return rst

        return sub(list(range(1, n+1)))

#Solution().generateTrees(3)
# @lc code=end
