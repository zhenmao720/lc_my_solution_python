class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def search(pos, _sum, _dif):
            row = len(pos)
            if row == n:
                result.append(pos)
            else:
                for col in xrange(n):
                    if col not in pos and row+col not in _sum and row-col not in _dif:
                        search(pos+[col], _sum+[row+col], _dif+[row-col])
        result = []
        search([], [], [])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in ans] for ans in result]    