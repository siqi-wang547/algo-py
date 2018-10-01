def wordBreakTopDown(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    def search(s, start, mem, word_dict):
        if start == len(s):
            return True
        if mem[start] != '*':
            return mem[start]
        for end in range(start+1, len(s)+1):
            if s[start:end] in word_dict:
                sr = search(s, end, mem, word_dict)
                if sr:
                    mem[start] = True
                    return mem[start]
        return mem[start]

    if not s and not wordDict:
        return True
    elif not s or not wordDict:
        return False
    word_dict = set(wordDict)
    mem = ['*'] * len(s)
    search(s, 0, mem, word_dict)
    return mem[0]


def wordBreakBottomUp(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    word_dict = set(wordDict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]


# print(wordBreakTopDown("aaaaaaa", ["aaa","aaaa"]))