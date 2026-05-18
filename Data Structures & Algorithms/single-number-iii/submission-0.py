class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        count = {}

        for  i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
        
        a=[]

        for i in count:
            if count[i] == 1:
                a.append(i)
        return a
        