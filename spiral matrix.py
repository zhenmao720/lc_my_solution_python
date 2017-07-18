class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==None or len(matrix)==0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        re = []
        while 2*(i+1) <= m and 2*(i+1) <= n:
            for j in range(i, n-i):
                re.append(matrix[i][j])
            for j in range(i+1, m-i):
                re.append(matrix[j][n-1-i])
            for j in range(n-2-i, i-1, -1):
                re.append(matrix[m-1-i][j])
            for j in range(m-2-i, i, -1):
                re.append(matrix[j][i])
            i += 1
        if 2 * i < n or 2 * j < m:
            for j in range(i, n - i):
                re.append(matrix[i][j])
            for j in range(i+1, m - i):
                re.append(matrix[j][n-1-i])
        return re