class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        
        for i in range(len(nums)):
            prefix.append(pre)
            pre *= nums[i]
                    
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= suf
            suf *= nums[i]

        return prefix