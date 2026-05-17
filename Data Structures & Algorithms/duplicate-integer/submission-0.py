class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count ={}
        for i in range(len(nums)):
            if nums[i]  in count:
                count[nums[i]]=count[nums[i]]+1
            else:
                count[nums[i]]=1
        for  i in count:
            if count[i] >=2:
                return True
        return False
        