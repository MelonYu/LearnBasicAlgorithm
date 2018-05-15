class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        f = 0
        r = len(nums)
        while f < r:
            if nums[f] == val:
                nums[f] = nums[r-1]
                r -= 1
            else:
                f += 1
        return r

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    print(s.removeElement(nums,val))
