#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (42.40%)
# Likes:    3279
# Dislikes: 167
# Total Accepted:    262.3K
# Total Submissions: 618.1K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rst = []
        if len(nums) <=k:
            return [max(nums)]
        d = deque()
        for i, v in enumerate(nums):
            if d and d[0] <= i-k:
                d.popleft()
            while d and nums[d[0]] <= v:
                d.popleft()
            while d and nums[d[-1]] <= v:
                d.pop()
            d.append(i)
            if i>= k-1:
                rst.append(nums[d[0]])
        return rst


# @lc code=end
