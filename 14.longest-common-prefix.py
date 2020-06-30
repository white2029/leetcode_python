#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.19%)
# Likes:    2518
# Dislikes: 1840
# Total Accepted:    747.3K
# Total Submissions: 2.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prs = ""
        if not strs:
            return prs
        while True:
            if i < len(strs[0]):
                prev = strs[0][i]
            else:
                return prs
            for s in strs[1::]:
                if i < len(s):
                    if prev != s[i]:
                        return prs
                else:
                    return prs
            prs += prev
            i += 1
        return prs

# @lc code=end
