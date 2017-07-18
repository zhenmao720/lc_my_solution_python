class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, front, end, step = len(nums), 0, 0, 0
        while end < l-1:
            step += 1
            maxend = end + 1
            for i in range(front, end+1):
                if i+nums[i] >= l-1:
                    return step
                maxend = max(maxend, i+nums[i])
            front, end = end+1, maxend
        return step