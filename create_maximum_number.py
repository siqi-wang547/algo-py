class Solution:
    def maxNum(self, nums1, nums2, k):
        """
        lc 321. create maximum number
        find the max number of length k constructed from digits from 2 given arrays
        the order of digits from a same given array should be preserved
        :param nums1:
        :param nums2:
        :param k:
        :return: a list of digits representing the max number
        """
        res = [0] * k
        for i in range(0, k+1):
            if i > len(nums1) or k - i > len(nums2):
                continue
            arr1, arr2 = self.findMaxSubarr(nums1, i), self.findMaxSubarr(nums2, k-i)
            res = max(res, self.merge(arr1, arr2, k))
        return res

    def merge(self, arr1, arr2, k):
        """
        merge two max subarray into a order-preserved subarray from digits of two arrays
        :param arr1:
        :param arr2:
        :param k:
        :return:
        """
        return [max(arr1, arr2).pop(0) for _ in range(k)]

    def findMaxSubarr(self, nums, k):
        """
        find a max subarray of length k from given array
        :param nums:
        :param k:
        :return:
        """
        res = []
        for i, num in enumerate(nums):
            while res and len(res) + len(nums) - i > k and res[-1] < nums[i]:
                res.pop()
            if len(res) < k:
                res.append(nums[i])
        return res