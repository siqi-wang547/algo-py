# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    """
    lc 173. Binary Search Tree Iterator
    implement hsaNext and next in average O(1) time and O(h) space

    the key to this solution is that even thought the next function has a while loop in it, the average
    time complexity is still O(1) for each node in the tree will only be visited exactly twice
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.addAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        if top.right:
            self.addAll(top.right)
        return top.val

    def addAll(self, root):
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left
