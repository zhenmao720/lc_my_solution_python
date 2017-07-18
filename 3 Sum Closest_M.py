class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        re = nums[0] + nums[1] + nums[len(nums)-1]
        for a in range(len(nums)-2):
            if a>0 and nums[a]==nums[a-1]:
                continue
            front, end = a+1, len(nums)-1
            while front<end:
                _sum = nums[a] + nums[front] + nums[end]
                if abs(_sum - target) < abs(re - target):
                    re = _sum
                    while front<end and nums[front]==nums[front+1]:
                        front += 1
                    while front<end and nums[end]==nums[end-1]:
                        end -= 1
                if _sum < target:
                    front += 1
                else:
                    end -= 1
        return re
        