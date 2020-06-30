#
# @lc app=leetcode id=1230 lang=python3
#
# [1230] Toss Strange Coins
#
# https://leetcode.com/problems/toss-strange-coins/description/
#
# algorithms
# Medium (47.83%)
# Likes:    95
# Dislikes: 4
# Total Accepted:    4.1K
# Total Submissions: 8.6K
# Testcase Example:  '[0.4]\n1'
#
# You have some coins.  The i-th coin has a probability prob[i] of facing heads
# when tossed.
#
# Return the probability that the number of coins facing heads equals target if
# you toss every coin exactly once.
#
#
# Example 1:
# Input: prob = [0.4], target = 1
# Output: 0.40000
# Example 2:
# Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# Output: 0.03125
#
#
# Constraints:
#
#
# 1 <= prob.length <= 1000
# 0 <= prob[i] <= 1
# 0 <= target <= prob.length
# Answers will be accepted as correct if they are within 10^-5 of the correct
# answer.
#
#
#

# @lc code=start
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        rev = [1]
        for x in reversed(prob):
            rev.append(rev[-1]*(1-x))
        rev = list(reversed(rev))
        if target == 0:
            return rev[0]
        prb = 0
        p = [1]
        for xi, x in enumerate(prob):
            np = []
            for i,v in enumerate(p):
                if i == 0:
                    np.append(v * (1-x))
                else:
                    np.append(v*(1-x) + p[i-1]*x)
            np.append(p[-1]*x)
            if len(np) > target:
                prb += np[target] * rev[xi+1]
            p = np[0:target]
        return prb





# @lc code=end
