class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        result = 0
        for x in range(len(nums)):
            if target == nums[x]:
                result = x
                break
            elif target < nums[x]:
                result = x
                break
            else:
                result = x + 1

        return result