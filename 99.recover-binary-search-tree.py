#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (38.98%)
# Likes:    1472
# Dislikes: 70
# Total Accepted:    161.3K
# Total Submissions: 413.5K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
#
# Input: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# Output: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# Example 2:
#
#
# Input: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# Output: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
#
# Follow up:
#
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ld = dict()
        rd = dict()
        ld[None] = 0
        rd[None] = 0
        vals = []
        def helper(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                ld[node] = 0
                rd[node] = 0
                vals.append(node.val)
                return
            helper(node.left)
            helper(node.right)
            ld[node] = ld[node.left] + rd[node.left] + (node.left is not None)
            rd[node] = ld[node.right] + rd[node.right] + (node.right is not None)
            vals.append(node.val)
        helper(root)
        svals = sorted(vals)
        #print(svals)
        #print({k.val: v for k,v in ld.items() if k})
        #print({k.val: v for k,v in rd.items() if k})
        def recover(sv, node):
            if not sv:
                return
            if len(sv) == 1:
                node.val = sv[0]
                return
            lc = ld[node]
            node.val = sv[lc]
            recover(sv[0:lc], node.left)
            recover(sv[lc+1::], node.right)
        recover(svals, root)

# @lc code=end
