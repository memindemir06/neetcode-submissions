class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in nums_map:
                return [nums_map[diff], idx]

            nums_map[num] = idx

        return []