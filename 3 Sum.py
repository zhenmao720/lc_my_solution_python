class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        re = []
        for i in xrange(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            front, end = i+1, len(nums)-1
            while front<end:
                target = nums[front]+nums[end]+nums[i]
                if target==0:
                    re.append([nums[front], nums[end], nums[i]])
                    while front<end and nums[front]==nums[front+1]:
                        front += 1
                    while front<end and nums[end] == nums[end-1]:
                        end -= 1
                    front += 1
                    end -= 1
                else:
                    if target<0:
                        front += 1
                    else:
                        end -= 1        
        return re
                    
