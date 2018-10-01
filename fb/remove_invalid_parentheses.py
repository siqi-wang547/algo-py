import collections

def removeInvalidParentheses(s):
    def valid(s):
        cnt = 0
        for ch in s:
            if ch == '(': cnt += 1
            elif ch == ')':
                cnt -= 1
                if cnt < 0: return False
        return cnt == 0

    q, visited, res = collections.deque(), set(), []
    q.append(s)
    visited.add(s)
    found = False

    while q:
        string = q.popleft()
        if valid(string):
            found = True
            res.append(string)
        if found:
            continue  # use found to ensure BFS will not go to the next level of traversal and thus the least removal
            # if the correct answers are in the current level, it's not possible to have other correct answers in the
            # next level since a valid string has to remove at least a pair of '()' to get another valid string
        for i in range(len(string)):
            if string[i] == '(' or string[i] == ')':
                tmp = string[:i] + (string[i+1:] if i < len(string) - 1 else '')
                if tmp not in visited:
                    q.append(tmp)
                    visited.add(tmp)
    return res


print(removeInvalidParentheses("()())()"))
