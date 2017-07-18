class Solution(object):
    def backtrack(self, re_ls, temp_ls, target, start, candidates):
        if target<0:
            return
        if target==0:
            re_ls.append(temp_ls)
        else:
            for i in range(start, len(candidates)):
                self.backtrack(re_ls, temp_ls+[candidates[i]], target-candidates[i], i, candidates)
                
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        re = []
        self.backtrack(re, [], target, 0, candidates)
        return re