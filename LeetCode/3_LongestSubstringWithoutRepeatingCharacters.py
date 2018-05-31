# -*- coding=utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符串长度
        n = len(s)
        # 可能的最大子串的起始位置
        i = 0
        
        # 最大长度
        ans = 0
        
        # 字符串以字典形式存储，可以去除重复的字符 s[j]:j+1
        dict_s = {}
        
        for j in range(0,(n)):
            if s[j] in dict_s.keys():
                # 已有重复字符时，更新子串的起始位置
                # 为当前重复字符的位置的下一位，且i应当是递增的
                i = max(i, dict_s[s[j]])
            # 计算此时的子串的最大长度
            ans = max(ans,j-i+1)
            # 加入不重复的字符或更新已重复字符的位置
            dict_s[s[j]] = j+1
            
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = 'pwwkew'
    print(sol.lengthOfLongestSubstring(s))
