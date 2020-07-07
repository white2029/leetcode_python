#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (45.00%)
# Likes:    1520
# Dislikes: 110
# Total Accepted:    461.1K
# Total Submissions: 1M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        rst_head = ListNode(-1)
        rst = rst_head
        curr = head
        while curr:
            check = curr
            while check and curr.val == check.val:
                check = check.next

            new_rst = ListNode(curr.val)
            rst.next = new_rst
            rst = new_rst

            if check is None:
                return rst_head.next
            curr = check

        return rst_head.next
# @lc code=end
