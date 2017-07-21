class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        re = []
        self.dfs(re, [], target, 0, candidates)
        return re
        
    def dfs(self, re_ls, temp_ls, remain, start, candidates):
        if remain==0:
            re_ls.append(temp_ls)
            return
        else:
            for i in range(start, len(candidates)):
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                elif candidates[i] > remain:
                    break
                else:
                    self.dfs(re_ls, temp_ls+[candidates[i]], remain-candidates[i], i+1, candidates)
        