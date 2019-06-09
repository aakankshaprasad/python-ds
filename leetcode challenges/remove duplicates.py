class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        # while (index < len(nums)-1):
        #     if(nums[index]==nums[index+1]):
        #         nums.pop(index)
        #     else:
        #         index+=1
        # return(len(nums))
        if len(nums)==0:
            return 0
        else:
            for i, c in enumerate(nums,1):
                if(i!=len(nums)):
                    if nums[i]!=nums[index]:
                        index+=1
                        nums[index]=nums[i]

            return index+1