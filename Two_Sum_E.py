class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}
        for i in range(len(nums)):
            if target-nums[i] in elements:
                return [elements[target-nums[i]], i]
            else:
                elements[nums[i]] = i
