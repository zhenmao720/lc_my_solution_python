class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        re = []
        for a in xrange(len(nums)-3):
            if a>0 and nums[a-1]==nums[a]:
                continue
            for b in xrange(a+1, len(nums)-2):
                if b > a+1 and nums[b-1] == nums[b]:
                    continue
                front, end = b+1, len(nums)-1
                while front<end:
                    s = nums[a]+nums[b]+nums[front]+nums[end]
                    if s == target:
                        re.append([nums[a], nums[b], nums[front], nums[end]])
                        while front<end and nums[front]==nums[front+1]:
                            front += 1
                        while front<end and nums[end]==nums[end-1]:
                            end -= 1
                        front += 1
                        end -= 1
                    else:
                        if s<target:
                            front += 1
                        else:
                            end -= 1
        return re
        