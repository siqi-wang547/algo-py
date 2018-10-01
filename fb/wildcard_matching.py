class Solution:
    """
    LC44. Wildcard Matching
    """
    def isMatchRecursive(self, s, p):
        if not p:
            return not s
        if p[0] == '*':
            return self.isMatchRecursive(s, p[1:]) or self.isMatchRecursive(s[1:], p)
        else:
            return p[0] in [s[0], '?'] and self.isMatchRecursive(s[1:], p[1:])

if __name__ == '__main__':
    s = Solution()
    print(s.isMatchRecursive('aa', '*'))