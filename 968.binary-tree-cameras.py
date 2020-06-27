#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (36.86%)
# Likes:    686
# Dislikes: 14
# Total Accepted:    18.6K
# Total Submissions: 50.2K
# Testcase Example:  '[0,0,null,0,0]'
#
# Given a binary tree, we install cameras on the nodes of the tree. 
#
# Each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
#
# Example 1:
#
#
#
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
#
# Example 2:
#
#
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Note:
#
#
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.
#
#
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
    def minCameraCover(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def mon(node):
            if node.left is None and node.right is None:
                return 1, 1, 0 # self installed, assumed covered by child, assumed covered by parents
            if node.left is None:
                ri, rc, rp = mon(node.right)
                return min([ri, rp, rc])+1, ri, min(ri, rc)
            if node.right is None:
                li, lc, lp = mon(node.left)
                return min([li, lp, lc])+1, li, min(li, lc)
            li, lc, lp = mon(node.left)
            ri, rc, rp = mon(node.right)
            return min([li, lp, lc]) +  min([ri, rc, rp]) + 1, min(ri + min([li, lc]), li + min([ri, rc])), min(ri, rc) + min(li, lc)

        i,c,p = mon(root)
        return min([i, c, p+1])




# @lc code=end
