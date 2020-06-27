#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (45.40%)
# Likes:    2525
# Dislikes: 42
# Total Accepted:    285.5K
# Total Submissions: 628.2K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        hq = []
        for s, e in intervals:
            heappush(hq, (s, 1))
            heappush(hq, (e, -1))

        rooms = 0
        max_room = 0
        while hq:
            _, val = heappop(hq)
            rooms += val
            max_room = max(max_room, rooms)
        return max_room





# @lc code=end
