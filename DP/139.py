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

