class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()
        for el in nums:
            if el in number_set:
                return True
            else:
                number_set.add(el)
        return False