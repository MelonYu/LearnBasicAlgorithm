'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: # return 0 when needle is an empty string.
        	return 0

        h = 0
        n = 0
        while h <= len(haystack) - len(needle):
        	s = 0
        	for n in range(len(needle)):
        		if haystack[h+n] != needle[n]:
        			break
        		else:
        			s += 1

        	if s == len(needle):
        		return h
        	else:
        		h += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    haystack = 'aaaaa'
    needle = 'baa'
    print(s.strStr(haystack, needle))        