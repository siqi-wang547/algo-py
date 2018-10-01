class Solution:
    def lengthOfLIS(self, nums):
        """
        lc 300. longest increasing subsequence
        Given an unsorted array of integers, find the length of longest increasing subsequence
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        dp = [1]
        for idx in range(1, len(nums)):
            prev_max_len = 0
            for prev_idx in range(idx):
                if nums[idx] > nums[prev_idx]:
                    prev_max_len = max(prev_max_len, dp[prev_idx])
            dp.append(prev_max_len + 1)
        return max(dp)

    def len_lis_2(self, nums):
        """
        O(nlgn) solution:
        arr tail[i] for smallest tail element of subsequence of length i + 1
        we can approve that array tail is non decreasing:
            for each pair of tail[i] and tail[i+1], the length of subsequence ending with tail[i] is smaller than
            that of tail[i+1] by 1. If tail[i] != tail[i+1], since tail[i] is either in or not in the subsequence
            ending with tail[i+1], if it's in, meaning tail[i] < tail[i+1] since the subsequence should be increasing
            and tail[i+1] is the last element; if it's not in, we can still prove it's not possible that tail[i] is
            larger because if it is, since tail[i] is either before or after tail[i+1], then ...
            array nums,
        :param nums:
        :return:
        """

        