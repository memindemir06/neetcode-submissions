class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            start = i + 1
            end = i + 1 + int(length)
            decoded.append(s[ start : end])
            i = i + 1 + int(length)

        return decoded