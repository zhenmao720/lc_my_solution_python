def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        ls = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m+1):
            ls[i][0] = i
        for i in xrange(n+1):
            ls[0][i] = i
        for i in xrange(0, m):
            for j in xrange(0, n):
                if word1[i] == word2[j]:
                    ls[i+1][j+1] = ls[i][j]
                else:
                    ls[i+1][j+1] = 1 + min(ls[i][j],ls[i+1][j],ls[i][j+1])
        return ls[m][n]