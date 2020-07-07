#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (49.70%)
# Likes:    2213
# Dislikes: 168
# Total Accepted:    464.3K
# Total Submissions: 931.3K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head

        def swap(prev,curr):
            if curr is None:
                return
            if curr.next is None:
                return

            secd = curr.next
            thrd = secd.next

            prev.next, curr.next, secd.next = secd, thrd, curr
            swap(curr, thrd)
        swap(dummy, head)
        return dummy.next

# @lc code=end
