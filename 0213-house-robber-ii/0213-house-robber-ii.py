# Time Complexity	: O(N)
# Space Complexity	: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], helper(nums[1:]), helper(nums[:len(nums)-1]))
    
def helper(nums):
    rob1 = 0
    rob2 = 0
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2