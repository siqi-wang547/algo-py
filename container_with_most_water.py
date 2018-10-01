def maxArea(self, height):
    """
    LC 11. Container With Most Water
    :type height: List[int]
    :rtype: int
    """

    """
    proof:
    suppose there is a solution to this question (al, ar) that makes the biggest container larger than our solution.
    Since the two pointer solution we provide will scan the all points and we haven't found the pair (al, ar),
    meaning when we never had (al, ar) at the same time. WLOG, suppose at the time left pointer meets al (al < ar)
    and right pointer hasn't met ar (there are only two starting condition, either when left meets al before right
    meets ar or when right meets ar before left meets al. They are actually same in terms of proof, so we choose one
    to start with).
    Until the end of iterations, there would be two circumstances:
    1. left pointer remains at al till the end, which means the right pointer must have visited ar and this contradicts
    to the assumption;
    2. left pointer moves when right pointer gets a height larger than height[al] at a_rr before it mets ar (otherwise
    contradiction same as 1). This time al and arr can already make a larger container than (al, ar). Contradict to
    the assumption that (al, ar) makes the optimal solution.
    """
    l, r = 0, len(height) - 1
    area = 0
    while l < r:
        area = max(area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area