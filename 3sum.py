class Solution:
    def triangleNumber(self, nums):
        """
        LC 611. Valid Triangle Number
        Given an array consists of non-negative integers, your task is to count the number of triplets chosen from
        the array that can make triangles if we take them as side lengths of a triangle.
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for last in range(len(nums)-1, 1, -1):
            l, r = 0, last - 1
            while l < r:
                if nums[l] + nums[r] > nums[last]:
                    # meaning index from l to r-1 can all be a valid first element of this triplet
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res
