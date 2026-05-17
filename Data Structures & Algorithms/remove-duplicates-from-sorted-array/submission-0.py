class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
                result.append(nums[i])

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)