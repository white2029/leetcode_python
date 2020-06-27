#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (34.83%)
# Likes:    3988
# Dislikes: 136
# Total Accepted:    398.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#

# @lc code=start
from functools import lru_cache
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsort = sorted(coins)
        coinset = set(coins)

        @lru_cache(None)
        def get(x):
            if x == 0:
                return 0
            if x in coinset:
                return 1
            min_coin = float('inf')
            for i in coinsort:
                if i > x:
                    return min_coin
                min_coin = min(min_coin, get(x-i)+1)
            return min_coin

        val = get(amount)
        return -1 if math.isinf(val) else val

# @lc code=end
