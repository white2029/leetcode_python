#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (31.01%)
# Likes:    1343
# Dislikes: 81
# Total Accepted:    149.8K
# Total Submissions: 482.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#

# @lc code=start
from collections import Counter
from functools import lru_cache

def debug(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        #print(*args, val)
        return val
    return wrapper

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cnt1 = Counter(s1)
        cnt2 = Counter(s2)
        cnt3 = Counter(s3)
        for k, v in cnt3.items():
            if v != cnt1[k] + cnt2[k]:
                return False

        @lru_cache(maxsize=None)
        def helper(i, j, k):
            if i<-1 or j<-1:
                return False
            if i==-1 and j==-1:
                return True
            if i==-1 and j==0:
                return s2[0] == s3[0]
            if i==0 and j==-1:
                return s1[0] == s3[0]

            val = False
            if i>=0 and s1[i] == s3[k]:
                val = val or helper(i-1, j, k-1)
            if j>=0 and s2[j] == s3[k]:
                val = val or helper(i, j-1, k-1)
            return val

        return helper(len(s1)-1, len(s2)-1, len(s3)-1)


# @lc code=end
