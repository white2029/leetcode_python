#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (40.82%)
# Likes:    1268
# Dislikes: 295
# Total Accepted:    213.9K
# Total Submissions: 520.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        large = ListNode(x)
        small = ListNode(x)
        ll, ss = large, small
        curr = head
        while curr:
            if curr.val < x:
                ss.next = curr
                ss = ss.next
            else:
                ll.next = curr
                ll = ll.next
            curr.next, curr = None, curr.next
        ss.next = large.next
        return small.next

# @lc code=end
