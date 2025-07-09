class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(0, n + 1):
            if i == 0 or i == 1:
                continue
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         pre, cur = 1, 1
#         if n <= 1:
#             return cur
#         while n > 1:
#             pre, cur = cur, cur + pre
#             n -= 1
#         return cur

print(Solution().climbStairs(3))

# 改进：不需要为整个数组，只需要两个变量
# => 斐波那契数列 => 矩阵+快速幂可以更快