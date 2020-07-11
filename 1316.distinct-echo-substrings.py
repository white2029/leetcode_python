#
# @lc app=leetcode id=1316 lang=python3
#
# [1316] Distinct Echo Substrings
#
# https://leetcode.com/problems/distinct-echo-substrings/description/
#
# algorithms
# Hard (46.49%)
# Likes:    65
# Dislikes: 110
# Total Accepted:    5.5K
# Total Submissions: 11.8K
# Testcase Example:  '"abcabcabc"'
#
# Return the number of distinct non-empty substrings of text that can be
# written as the concatenation of some string with itself (i.e. it can be
# written as a + a where a is some string).
#
#
# Example 1:
#
#
# Input: text = "abcabcabc"
# Output: 3
# Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
#
#
# Example 2:
#
#
# Input: text = "leetcodeleetcode"
# Output: 2
# Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 2000
# text has only lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        val = set()
        for i in range(1, int(len(text)/2)+1):
            prev = None
            for s1, v in enumerate(text):
                s2 = s1 + i
                if prev is not None and prev + i == s1:
                    val.add(text[prev:s1])
                    prev += 1
                if s2 >= len(text):
                    break
                if text[s2] == v:
                    if prev is None:
                        prev = s1
                else:
                    prev = None
        #print(val)
        return len(val)





# @lc code=end
