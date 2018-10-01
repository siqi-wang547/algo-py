
class Solution:
    def longestValidParentheses(self, s):
        """
        LC 32. Longest Valid Parentheses
        given a string containing only '(' and ')', find out the length of the longest valid parentheses substring
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        for idx, ch in enumerate(s):
            if idx > 0 and ch == ')' and s[idx-1] == '(':
                dp[idx] = 2 if idx == 1 else dp[idx-2] + 2
            elif idx > 0 and ch == ')' and s[idx-1] == ')':
                if idx-dp[idx-1]-1 >= 0 and s[idx-dp[idx-1]-1] == '(':
                    dp[idx] = dp[idx-1] + 2 + (dp[idx-dp[idx-1]-2] if (dp[idx-dp[idx-1]-2] > 0) else 0)
        return max(dp)

    def solution2(self, s):
        if not s:
            return 0
        stack = [-1]
        max_res = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_res = max(max_res, idx - stack[-1])
        return max_res

    def solution3(self, s):
        if not s:
            return 0
        counter, res, start = 0, 0, -1
        for idx, ch in enumerate(s):
            if ch == '(':
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    res = max(res, idx - start)
                elif counter < 0:
                    start = idx
                    counter = 0
        if counter > 0:
            # 只有当左括号比右括号多的时候才需要进行第二次循环
            # 原因是假如整个str中左括号仅比右括号多一个，从多余的这个左括号开始向右遍历时都无法reach到counter == 0这个条件
            # 又因为左括号比右括号仅多一个，所以从这个多余到括号后一位起到结尾必定是一个valid substring
            # 我们从右向左遍历一次即可得知这个valid substring的长度，和之前求得的长度相比较即可知道全局的最长解
            counter, start = 0, len(s)
            for idx in range(0, len(s), -1):
                if s[idx] == ')':
                    counter += 1
                else:
                    counter -= 1
                    if counter == 0:
                        res = max(res, start - idx)
                    elif counter < 0:
                        start = idx
                        counter = 0
        return res