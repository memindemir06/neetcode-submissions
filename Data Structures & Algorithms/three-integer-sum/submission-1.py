class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i in range(len(nums)):
            target = nums[i]

            left = i+1
            right = len(nums) - 1

            while left < right and target <= 0:
                threeSum = nums[left] + nums[right] + target
                if threeSum == 0:
                    result.append((target, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
        return list(set(result))         

