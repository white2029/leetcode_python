#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (34.56%)
# Likes:    445
# Dislikes: 18
# Total Accepted:    33.8K
# Total Submissions: 97.8K
# Testcase Example:  '"aabbcc"\n3'
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
#
# Example 1:
#
#
#
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
#
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.
#
#
#
# Example 3:
#
#
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
#
#
#
#
#

# @lc code=start
from collections import deque, Counter
from heapq import heappush, heappop
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        hq = []
        q = deque()
        cnt = Counter(s)
        for i,c in cnt.items():
            heappush(hq, (-c, i))
        for i in range(0, k-1):
            q.append(None)
        rst = ""
        tie = 0
        while hq:
            tie += 1
            #print('before', hq, q, rst)
            c, v = heappop(hq)
            rst += v
            val = None

            val = q.popleft()
            if val:
                heappush(hq, val)
            if c + 1 < 0:
                q.append((c+1, v))
            else:
                q.append(None)

            #print('after', hq, q, rst)
        return rst if len(rst) == len(s) else ""



# @lc code=end
