#
# @lc app=leetcode id=582 lang=python3
#
# [582] Kill Process
#
# https://leetcode.com/problems/kill-process/description/
#
# algorithms
# Medium (60.00%)
# Likes:    457
# Dislikes: 11
# Total Accepted:    33.1K
# Total Submissions: 55.1K
# Testcase Example:  '[1,3,10,5]\n[3,0,5,3]\n5'
#
# Given n processes, each process has a unique PID (process id) and its PPID
# (parent process id).
#
# Each process only has one parent process, but may have one or more children
# processes. This is just like a tree structure.  Only one process has PPID
# that is 0, which means this process has no parent process. All the PIDs will
# be distinct positive integers.
#
# We use two list of integers to represent a list of processes, where the first
# list contains PID for each process and the second list contains the
# corresponding PPID.
# ⁠
# Now given the two lists, and a PID representing a process you want to kill,
# return a list of PIDs of processes that will be killed in the end. You should
# assume that when a process is killed, all its children processes will be
# killed. No order is required for the final answer.
#
# Example 1:
#
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation:
# ⁠          3
# ⁠        /   \
# ⁠       1     5
# ⁠            /
# ⁠           10
# Kill 5 will also kill 10.
#
#
#
# Note:
#
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.
#
#
#

# @lc code=start
from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        cd = defaultdict(set)
        for i, c in enumerate(pid):
            p = ppid[i]
            cd[p].add(c)
        rst = set()
        to_visit = {kill}
        while to_visit:
            new_visit = set()
            for p in to_visit:
                rst.add(p)
            for p in to_visit:
                new_visit.update(cd[p])
            new_visit.difference_update(rst)
            to_visit = new_visit
        return list(rst)
# @lc code=end
