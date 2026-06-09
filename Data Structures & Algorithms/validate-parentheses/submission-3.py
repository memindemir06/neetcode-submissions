class Solution:
    def isValid(self, s: str) -> bool:
        def matches(opened, closed):
            if ((opened == '(' and closed == ')')
                or (opened == '{' and closed == '}')
                or (opened == '[' and closed == ']')):
                return True
            return False
        brackets = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                brackets.append(char)
            if char == ')' or char == ']' or char == '}':
                if len(brackets) == 0:
                    return False
                else:
                    match = brackets.pop()
                    if not matches(match, char):
                        return False
        if len(brackets) > 0:
            return False
        return True