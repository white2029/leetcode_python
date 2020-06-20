#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (55.08%)
# Likes:    1443
# Dislikes: 56
# Total Accepted:    486.1K
# Total Submissions: 882.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        rst = []
        curr = root
        q = deque()
        while True:
            if curr is not None:
                rst.append(curr.val)
                if curr.right:
                    q.append(curr.right)
                curr = curr.left
            else:
                if q:
                    curr = q.pop()
                else:
                    break
        return rst

# @lc code=end
