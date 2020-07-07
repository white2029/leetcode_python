#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (36.26%)
# Likes:    1648
# Dislikes: 106
# Total Accepted:    248.5K
# Total Submissions: 681.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
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
            cnt = 0
            while check and curr.val == check.val:
                check = check.next
                cnt += 1

            if cnt > 1:
                curr = check
                continue

            new_rst = ListNode(curr.val)
            rst.next = new_rst
            rst = new_rst

            if check is None:
                return rst_head.next
            curr = check

        return rst_head.next
# @lc code=end
