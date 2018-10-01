class Trie(object):
    class TrieNode:
        def __init__(self):
            self.is_leaf = False
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            cur.children.setdefault(c, Trie.TrieNode())  # important, cannot reinitialize a previously defined node
            cur = cur.children[c]
        cur.is_leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:

            if not cur.children.get(c):
                return False
            else:
                cur = cur.children[c]
        return cur.is_leaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if not cur.children.get(c):
                return False
            else:
                cur = cur.children[c]
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)