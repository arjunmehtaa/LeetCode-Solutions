class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
        return ans
                
        