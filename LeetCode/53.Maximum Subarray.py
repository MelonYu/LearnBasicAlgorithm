class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

if __name__ == '__main__':
    S = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(S.maxSubArray(nums)) # should be 6
