class Solution:
    """
    LC10. Regular Expression Matching

    """

    def isMatchRecursive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        match_first = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.isMatchRecursive(s, p[2:]) or (match_first and self.isMatchRecursive(s[1:], p))
        else:
            return match_first and self.isMatchRecursive(s[1:], p[1:])

    def isMatchTopDown(self, s, p):
        pass

    def isMatchBottomUp(self, s, p):
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match_first = i < len(s) and p[j] in [s[i], '.']
                if j + 1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or match_first and dp[i+1][j]
                else:
                    dp[i][j] = match_first and dp[i+1][j+1]
        return dp[0][0]
