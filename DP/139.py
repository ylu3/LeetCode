from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        @cache
        def wordBreak_internal(s: str):
            if not s:
                return True
            for i in range(len(s)):
                if s[:i+1] in d and wordBreak_internal(s[i+1:]):
                    return True
            return False

        return wordBreak_internal(s)

        # 根据最大单词长度剪枝
        # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #     d = set(wordDict)
        #     k = max(len(w) for w in wordDict)
        #     @cache
        #     def wordBreak_internal(s: str):
        #         if not s:
        #             return True
        #         for i in range(len(s)):
        #             if i + 1 > k:
        #                 break
        #             if s[:i+1] in d and wordBreak_internal(s[i+1:]):
        #                 return True
        #         return False
        #
        #     return wordBreak_internal(s)


print(Solution().wordBreak("applepenapple", ["apple","pen"]))

# 没有缓存的情况下，本质上是生成字符串所有的分割方式（数量不限），每一个位置可以选择割与不割，因此复杂度为2**n
# 如果缓存那么在最外层循环的第一次（i=0）结束后就会覆盖所有可能的wordBreak_internal(i)，因此递归最外层i>1之后都是O(1)
# 假设长度为L的字符串的时间复杂度F(L)， F(L) = F(L-1) + O(n) = (F(L-2) + O(n-1)) + O(n) .... => O(n**2)
# F(L-1)对应i = 0，O(n)对应i > 1
# 以上均为最坏情况，例如dict中有所有源字符串的字符的任意组合，但是少某一个字符