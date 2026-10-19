class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {'{':'}', '(':')', '[':']'}
        stack = []

        for ch in s:
            if ch in parentheses.keys():
                stack.append(ch)
            else:
                if stack:
                    opening = stack.pop()
                    if ch!=parentheses[opening]:
                        return False
                else:
                    return False
        return True if not stack else False