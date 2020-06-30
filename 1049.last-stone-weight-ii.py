#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
# https://leetcode.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (43.80%)
# Likes:    596
# Dislikes: 26
# Total Accepted:    16.4K
# Total Submissions: 37.4K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose any two rocks and smash them together.  Suppose the
# stones have weights x and y with x <= y.  The result of this smash is:
#
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
#
#
# At the end, there is at most 1 stone left.  Return the smallest possible
# weight of this stone (the weight is 0 if there are no stones left.)
#
#
#
# Example 1:
#
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the
# optimal value.
#
#
#
#
# Note:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100
#
#

# @lc code=start

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sx = sorted(stones)
        ttl = sum(stones) // 2
        if ttl == 0:
            return 0

        min_diff = float('inf')
        vals = {0}
        for i in sx:
            if i > ttl:
                break
            to_add = set()
            for j in vals:
                t = i + j
                if t in vals or t in to_add:
                    continue
                d = ttl - t
                if d == 0:
                    return sum(stones) - ttl - ttl
                if d > 0:
                    if d < min_diff:
                        min_diff = d
                    to_add.add(t)
            vals.update(to_add)
        #print(ttl, sum(stones), min_diff)
        return sum(stones) - (ttl-min_diff)*2



# @lc code=end
