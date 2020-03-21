"""
Time Complexity: O(N^2)
Space Complexity: O(N) As we are making use of the DP Array
Compiled on Leetcode?: Yes
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maximum = 1
        dp = [ 1 for i in range(len(nums))]
        count = 0
        for i in range(1, len(nums)):
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    maximum = max(maximum, dp[i])
        return maximum