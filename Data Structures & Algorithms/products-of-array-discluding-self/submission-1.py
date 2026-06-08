class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        start = 0
        end = len(nums) - 1

        pre = 1
        suf = 1

        while start < len(nums):
            prefix.append(pre)
            pre *= nums[start]
            start += 1

            suffix.insert(0,suf)
            suf *= nums[end]
            end -= 1
        
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result