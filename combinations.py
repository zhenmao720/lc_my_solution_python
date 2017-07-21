class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        re = []
        self.dfs(re, [], 1, n, 0, k)
        return re
    
    def dfs(self, re_ls, temp_ls, start, n, l, target):
        if l == target:
            re_ls.append(temp_ls)
        else:
            for i in xrange(start, n-target+l+2):
                self.dfs(re_ls, temp_ls + [i], i + 1, n, l+1, target)
