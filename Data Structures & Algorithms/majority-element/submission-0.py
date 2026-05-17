class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
        max_count=0
        result = 0
        for i in count:
            if count[i] > max_count:
                max_count = count[i]
                result = i
        return result
        