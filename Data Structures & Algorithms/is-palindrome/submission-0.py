class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        processed = pattern.sub('', s).lower()

        if len(processed) == 1:
            return True

        left = (len(processed) - 1) // 2
        right = left if len(processed) % 2 else left + 1

        while left >= 0 and right < len(processed):
            if processed[left] != processed[right]:
                return False
            left -= 1
            right += 1

        return True
