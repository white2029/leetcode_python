#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (36.22%)
# Likes:    313
# Dislikes: 501
# Total Accepted:    97.5K
# Total Submissions: 269.1K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 0, 1, 3, 5, 6 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note:
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# Follow up:
# 
# 
# This is a follow up problem to H-Index, where citations is now guaranteed to
# be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
# 
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations) -> int:
        if not citations:
            return 0

        l, r = 0, len(citations) - 1
        lth = len(citations)

        while l <= r:
            m = l + (r-l)//2
            if citations[m] > lth-m:
                r = m - 1
            elif citations[m] == lth-m:
                return lth - m
            else:
                l = m + 1

        return lth - l

#print(Solution().hIndex([0,1,3,5,6]))
#print(Solution().hIndex([0, 0, 0]))
#print(Solution().hIndex([100]))
# @lc code=end
