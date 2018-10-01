def longestPalindrome(s):
    """
    LC5. Longest Palindromic Substring
    :type s: str
    :rtype: str
    """
    s_len = len(s) 
    sr = s[::-1]
    max_len, start = 0, 0
    dp_matrix = [[0] * (s_len + 1) for _ in range(s_len + 1)]
    for i in range(s_len):
        for j in range(s_len):
            if s[i] == sr[j]:
                dp_matrix[i + 1][j + 1] = dp_matrix[i][j] + 1
                if dp_matrix[i + 1][j + 1] > max_len and is_palin(s, i + 1 - dp_matrix[i + 1][j + 1], i):
                    max_len = dp_matrix[i + 1][j + 1]
                    start = i + 1 - max_len

    return s[start:start + max_len]


def is_palin(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def longestPalindrome2(s):
    def expand(s, left, right):
        max_len = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            max_len = right - left + 1
            left -= 1
            right += 1
        return max_len, left + 1

    max_len, start = 0, 0
    for i in range(len(s)):
        len1, st1 = expand(s, i, i)
        len2, st2 = expand(s, i, i + 1)
        if max(len1, len2) > max_len:
            max_len = max(len1, len2)
            start = st1 if len1 > len2 else st2
    return s[start:start + max_len]

print(longestPalindrome2("aacdefcaa"))