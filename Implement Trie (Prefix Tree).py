class Node(object):    
    def __init__(self, c):
        self.contant = c
        self.childlist = []
        self.isend = False
    
    def subNode(self, c):
        if self.childlist:
            for child in self.childlist:
                if child.contant == c:
                    return child
        return None

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(' ')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if self.search(word):
            return
        cur = self.root
        for i in xrange(len(word)):
            child = cur.subNode(word[i])
            if child:
                cur = child
            else:
                newchild = Node(word[i])
                cur.childlist.append(newchild)
                cur = newchild
        cur.isend = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in xrange(len(word)):
            child = cur.subNode(word[i])
            if not child:
                return False
            else:
                cur = child
        if cur.isend:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in xrange(len(prefix)):
            child = cur.subNode(prefix[i])
            if not child:
                return False
            else:
                cur = child
        return True