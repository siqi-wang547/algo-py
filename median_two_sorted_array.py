
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # we need to keep len(nums2) >= len(nums1)

    m, n = len(nums1), len(nums2)
    if m > n:
        m, n, nums1, nums2 = n, m, nums2, nums1

    left, right = 0, m  # there are m + 1 dividing points from 0 ~ m, nums1 left = nums1[0:m-1]
    half_total_len = ((m + n + 1) / 2)

    while left <= right:
        div_p = int((left + right) / 2)
        div_q = half_total_len - div_p
        if div_p > 0 and div_q < n and nums1[div_p - 1] > nums2[div_q]:
            right = div_p - 1
        elif div_p < m and div_q > 0 and nums1[div_p] < nums2[div_q - 1]:
            left = div_p + 1
        else:
            if div_p == 0:
                left_max = nums2[div_q - 1]
            elif div_q == 0:
                left_max = nums1[div_p - 1]
            else:
                left_max = max(nums1[div_p - 1], nums2[div_q - 1])

            if (m + n) % 2 > 0:
                return left_max

            if div_p == m:
                right_min = nums2[div_q]
            elif div_q == n:
                right_min = nums1[div_p]
            else:
                right_min = min(nums1[div_p], nums2[div_q])
            return (left_max + right_min) / 2

if __name__ == '__main__':
    nums1, nums2 = [1,3], [2]
    print(findMedianSortedArrays(nums1, nums2))