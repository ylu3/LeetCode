from functools import cache
from typing import List


# 没有记忆化搜素是n**2的复杂度，超时
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         l = len(nums)
#         if l == 1:
#             return nums[0]
#         if l == 2:
#             return max(nums[0], nums[1])
#         return max(nums[-1]+ self.rob(nums[:l-2]), self.rob(nums[:l-1]))

# 因为要cache所以只能传递索引
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         @cache
#         def rob_internal(i: int):
#             if i == 0:
#                 return nums[0]
#             if i == 1:
#                 return max(nums[0], nums[1])
#             return max(nums[i] + rob_internal(i-2), rob_internal(i-1))
#         return rob_internal(len(nums) -1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        for i in range(l):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

print(Solution().rob([1,2,3,1]))
