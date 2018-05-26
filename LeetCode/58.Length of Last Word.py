'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

Note: A word is defined as a character sequence consists of non-space characters only.

'''

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list( map(str,s.strip()))
        if not len(s):
            return 0
        s = ''.join(s)
        l = list(map(len,s.split(' ')))
        return l[-1]

if __name__ == '__main__':
    words = '  I Love You  '
    s = Solution()
    last = s.lengthOfLastWord(words)
    print(last)

