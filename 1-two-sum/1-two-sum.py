class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [i, dict[nums[i]]]
            num_to_find = target - nums[i]
            dict[num_to_find] = i
        