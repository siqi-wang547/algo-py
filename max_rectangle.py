"""
LC85. Maximal Rectangle
/* we start from the first row, and move downward;
 * height[i] record the current number of countinous '1' in column i;
 * left[i] record the left most index j which satisfies that for any index k from j to  i, height[k] >= height[i];
 * right[i] record the right most index j which satifies that for any index k from i to  j, height[k] >= height[i];
 * by understanding the definition, we can easily figure out we need to update maxArea with value (height[i] * (right[i] - left[i] + 1));
 *
 * Then the question is how to update the array of height, left, and right
 * =================================
 * for updating height, it is easy
 * for (int j = 0; j < n; j++) {
 *    if (matrix[i][j] == '1') height[j]++;
 *    else height[j] = 0;
 * }
 * =============================================================================
 * It is a little bit tricky for initializing and updating left and right array
 * for initialization:
 * we know initially, height array contains all 0, so according to the definition of left and right array, left array should contains all 0, and right array should contain all n - 1
 * for updating left and right, it is kind of tricky to understand...
 *     ==============================================================
 *     Here is the code for updating left array, we scan from left to right
 *     int lB = 0;  //lB is indicating the left boundry for the current row of the matrix (for cells with char "1"), not the height array...
 *     for (int j = 0; j < n; j++) {
 *          if (matrix[i][j] == '1') {
 *              left[j] = Math.max(left[j], lB); // this means the current boundry should satisfy two conditions: within the boundry of the previous height array, and within the boundry of the current row...
 *          } else {
 *              left[j] = 0; // when matrix[i][j] = 0, height[j] will get update to 0, so left[j] becomes 0, since all height in between 0 - j satisfies the condition of height[k] >= height[j];
 *              lB = j + 1; //and since current position is '0', so the left most boundry for next "1" cell is at least j + 1;
 *          }
 *     }
 *     ==============================================================
 *     the idea for updating the right boundary is similar, we just need to iterate from right to left
 *     int rB = n - 1;
 *     for (int j = n - 1; j >= 0; j--) {
 *         if (matrix[i][j] == '1') {
 *              right[j] = Math.min(right[j], rB);
 *         } else {
 *              right[j] = n - 1;
 *              rB = j - 1;
 *      }
 */
"""


def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    m, n, max_area = len(matrix), len(matrix[0]), 0

    heights, left, right = [0] * n, [0] * n, [n - 1] * n

    for i in range(m):
        right_bound = n - 1
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], right_bound)
            else:
                right[j] = n - 1
                right_bound = j - 1
        left_bound = 0
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
                left[j] = max(left[j], left_bound)
                max_area = max(max_area, heights[j] * (right[j] - left[j] + 1))
            else:
                left[j] = 0
                heights[j] = 0
                left_bound = j + 1
    return max_area


"""
LC 84: Largest Rectangle in Histogram

A divide and conquer solution: as the area of a rectangle is confined by the min height in consecutive heights,
 we just need to find all those consecutive heights. we divide the problem into subproblem on a subset of the original
 heights array and solve them respectively. Time complexity average O(nlgn)
"""
def maxRectHistogram1(heights):
    if not heights:
        return 0

    def conquer(heights, left, right):
        if left > right:
            return 0
        min_idx = right
        for i in range(left, right):
            if heights[i] < heights[min_idx]:
                min_idx = i
        return max(heights[min_idx]*(right-left+1), conquer(heights, left, min_idx-1), conquer(heights, min_idx+1, right))
    return conquer(heights, 0, len(heights)-1)


"""
LC 84: Largest Rectangle in Histogram

A stack solution: we just need to find out for all each height that the rectangle use it as the shortest bar.
From left to right, we push every height into the stack. When we meet a shorter bar than the current stack peek, we
then find out all the area of the rectangle for the bars already in the stack by popping them out. Last, we use a the
same technique to pop out all elements left in the stack and calculate the max area.
"""
def maxRectHistogram(heights):
    if not heights:
        return 0
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
            max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    return max_area

"""
LC85. Maximal Rectangle
Solution based on LC84
"""
def maxRectMatrix(matrix):
    if not matrix or not matrix[0]:
        return 0
    heights = [0] * len(matrix[0])
    max_area = 0
    for row in matrix:
        for i in range(len(row)):
            heights[i] = heights + 1 if row[i] == '1' else 0
        max_area = max(max_area, maxRectHistogram(heights))

    return max_area